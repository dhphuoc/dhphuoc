import os
import asyncio
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

# Hàng đợi cho các yêu cầu xử lý chuyển xu
task_queue = asyncio.Queue()

# Dictionary lưu trạng thái dừng của từng người dùng
user_stop_events = {}

# Lưu thông tin tệp tài khoản
accounts_file = None


class TraoDoiSub_Api:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.headers = {
            'authority': 'traodoisub.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://traodoisub.com',
            'referer': 'https://traodoisub.com/',
            'x-requested-with': 'XMLHttpRequest'
        }

    def info(self):
        try:
            response = self.session.post(
                'https://traodoisub.com/scr/login.php', headers=self.headers,
                data={'username': self.username, 'password': self.password}).text

            if 'success' in response:
                user_info = self.session.get('https://traodoisub.com/scr/user.php', headers=self.headers)
                if user_info.ok:
                    user_data = user_info.json()
                    return True, self.username, int(user_data.get('xu', 0))
        except Exception as e:
            print(f"Lỗi info(): {e}")
        return False, None, None

    def chuyen(self, usernhan, xutang):
        try:
            response = self.session.post(
                'https://traodoisub.com/view/tangxu/tangxu.php', headers=self.headers,
                data={'usernhan': usernhan, 'xutang': xutang}).text

            return "Chuyển xu thành công!" if response.strip() == "3" else f"Lỗi: {response}"
        except Exception as e:
            print(f"Lỗi chuyen(): {e}")
            return "Lỗi trong quá trình chuyển xu."


def read_accounts(file_path):
    accounts = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                account = line.strip().split('|')
                if len(account) == 2:
                    accounts.append((account[0], account[1]))
    except Exception as e:
        print(f"Lỗi đọc tệp: {e}")
    return accounts


def mask_username(username):
    return username[:3] + "..." + username[-3:] if len(username) > 6 else username


async def stop(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    if user_id in user_stop_events:
        user_stop_events[user_id].set()
        await update.message.reply_text("Đã dừng theo dõi xu!", parse_mode="Markdown")


async def check_xu_continuously(update: Update, context: CallbackContext, usernhan: str, xu_tang: int):
    global accounts_file
    user_id = update.message.chat_id

    if user_id in user_stop_events:
        user_stop_events[user_id].clear()
    else:
        user_stop_events[user_id] = asyncio.Event()

    accounts = read_accounts(accounts_file)
    while not user_stop_events[user_id].is_set():
        for username, password in accounts:
            api = TraoDoiSub_Api(username, password)
            is_success, username, xu_balance = api.info()
            masked_username = mask_username(username)

            if is_success:
                xu_balance_formatted = "{:,}".format(xu_balance).replace(",", ".")
                if xu_balance >= 1100000:
                    result = api.chuyen(usernhan, xu_tang)
                    await update.message.reply_text(
                        f"*Chuyển xu thành công!* 🎉\nTừ tài khoản `{masked_username}`\n{result}",
                        parse_mode="Markdown")
                else:
                    await update.message.reply_text(
                        f"Tài khoản `{masked_username}` không đủ xu.\nSố dư: *{xu_balance_formatted}*.\n"
                        f"Đang tiếp tục kiểm tra...",
                        parse_mode="Markdown")

            else:
                await update.message.reply_text(f"Đăng nhập thất bại với tài khoản `{masked_username}`.",
                                                parse_mode="Markdown")

            await asyncio.sleep(5)  # Đợi 5 giây trước khi kiểm tra tài khoản tiếp theo

        await asyncio.sleep(5)  # Đợi 5 giây trước khi kiểm tra lại toàn bộ tài khoản


async def handle_document(update: Update, context: CallbackContext):
    global accounts_file
    file = update.message.document
    file_path = await file.get_file()
    file_name = file.file_name

    download_path = f'./{file_name}'
    await file_path.download_to_drive(download_path)
    accounts_file = download_path

    accounts = read_accounts(download_path)
    if accounts:
        await update.message.reply_text(f"Đã nhận tệp `{file_name}` với {len(accounts)} tài khoản.",
                                        parse_mode="Markdown")
    else:
        await update.message.reply_text(f"Tệp `{file_name}` không có tài khoản hợp lệ.", parse_mode="Markdown")


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Chào bạn! Hãy gửi tệp tài khoản (user|pass) để bot kiểm tra xu.")


async def transfer_xu(update: Update, context: CallbackContext):
    if accounts_file is None:
        await update.message.reply_text("*Lỗi:* Bạn cần tải lên tệp tài khoản trước.", parse_mode="Markdown")
        return

    if len(context.args) < 2:
        await update.message.reply_text("*Lỗi:* Bạn cần cung cấp đầy đủ lệnh:\n`/transfer_xu <usernhan> <xu>`",
                                        parse_mode="Markdown")
        return

    usernhan = context.args[0]
    try:
        xu_tang = int(context.args[1])
    except ValueError:
        await update.message.reply_text("*Lỗi:* Số xu phải là số nguyên hợp lệ.", parse_mode="Markdown")
        return

    await update.message.reply_text("Bắt đầu kiểm tra xu liên tục...", parse_mode="Markdown")

    # Đưa công việc vào hàng đợi để xử lý song song
    await task_queue.put((update, context, usernhan, xu_tang))


async def worker():
    while True:
        update, context, usernhan, xu_tang = await task_queue.get()
        await check_xu_continuously(update, context, usernhan, xu_tang)
        task_queue.task_done()


def main():
    application = Application.builder().token("YOUR_BOT_TOKEN").build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('transfer_xu', transfer_xu))
    application.add_handler(CommandHandler('stop', stop))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    # Chạy worker để xử lý hàng đợi
    asyncio.create_task(worker())

    application.run_polling()


if __name__ == '__main__':
    main()