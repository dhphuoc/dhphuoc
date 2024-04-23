import requests, os, sys, datetime
from time import sleep

os.system("cls" if os.name == "nt" else "clear")
def main():
    os.system("cls" if os.name == "nt" else "clear")
    count = 0;count1 = 0;block = 0;s = 0;dem_so_nv = 0
    tokentds = input('NHẬP ACCESS_TOKEN TDS: ')
    file = input('NHẬP FILE TOKEN PAGE: ')
    try:
        tokenfb_list = open(file).readlines()
    except:
        exit()
    for line in tokenfb_list:
        count += 1
    print(f'TÌM THẤY {count} TOKEN PAGE')
    file1 = input('NHẬP FILE UID PAGE: ')
    try:
        idfb_list = open(file1).readlines()
    except:
        exit()
    for line in idfb_list:
        count1 += 1
    print(f'TÌM THẤY {count1} UID PAGE')
    stop = int(input('NHẬP SỐ NHIỆM VỤ: '))
    stop_block = int(input('NHẬP SỐ LẦN VƯỢT BLOCK: '))
    accounts_count = len(tokenfb_list)
    tasks_per_account = 1
    while True:
        for account_index in range(accounts_count):
            tokenfb = tokenfb_list[account_index].strip()
            idfb = idfb_list[account_index].strip()
            os.system("cls" if os.name == "nt" else "clear")
            fb = requests.get('https://graph.facebook.com/me/?access_token='+str(tokenfb))
            if 'id' in fb.text and 'name' in fb.text:print(f"[ĐANG CẤU HÌNH: {str(fb.json()['name'].upper())} ID: {str(fb.json()['id'])}]")
            else:print(fb.json()["error"]["message"]);continue
            run = requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+str(tokentds))
            if 'success' in run.text:print(run.json()['data']["msg"].upper())
            else:print(run.json()['error'].upper());continue
            for task_index in range(1, tasks_per_account + 1):
                time = datetime.datetime.now().strftime("%H:%M:%S")
                while True:
                    listlike = requests.get('https://traodoisub.com/api/?fields=likesieure&access_token='+str(tokentds))
                    if 'id' in listlike.text:break
                snv = len(listlike.json())
                s = s+snv
                tsnv = s
                print(f'TÀI KHOẢN {account_index+1}/{accounts_count} - TÌM THẤY [{str(snv)}] NHIỆM VỤ [{time}]')
                for i in range(0, len(listlike.json()), 1):
                    dem_so_nv=tsnv-snv+i+1
                    id = listlike.json()[i]['id']
                    urllike = 'https://graph.facebook.com/'+str(id)+'/likes'
                    datalike = 'access_token=' + str(tokenfb)
                    like = requests.post(urllike, data=datalike)
                    if like.text == 'true':pass
                    if 'error' in like.text and '368' in like.text:block = block + 1
                    if block == stop_block:break
                    if 'error' in like.text and '190' in like.text:break
                    nhanxu = requests.get('https://traodoisub.com/api/coin/?type=LIKESIEURE&id='+str(id)+'&access_token='+str(tokentds))
                    xu = nhanxu.json()
                    if 'success' in xu:print(xu)
                    if 'error' in xu:pass
                    if (tsnv - snv + i + 1) == stop:break
                if block == stop_block:break
                if (tsnv - snv + i + 1) == stop:break
                if 'error' in like.text and '190' in like.text:break
                for delay in range(3, 0, -1):
                    print(f'[DHP07] ĐANG GET LIST NHIỆM VỤ, ĐỢI: {delay}')
                    sleep(0.7)
            if task_index == tasks_per_account:
                print(f"CHUYỂN SANG TÀI KHOẢN TIẾP THEO...")
                break
            if account_index == accounts_count - 1:
                account_index = -1
                tokenfb = tokenfb_list[0]
                idfb = idfb_list[0]
                continue
        ttacc = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(tokentds)).json()
        print(f"TỔNG XU CỦA TÀI KHOẢN HIỆN TẠI: {str(ttacc['data']['xu'])}")

if __name__ == '__main__':
    ip = int(requests.get('https://ipinfo.io/json').json()['ip'].replace('.', ''))
    key_time = datetime.datetime.now()
    d = key_time.day
    m = key_time.month
    y = key_time.year
    get_key = f'{d * 5}{int(y/20)*5}{(ip//y)*d//m}'
    key = get_key.split()
    get_linkocto = requests.get(f'https://octolinkz.com/api?api=53391e62b871e9c387067f2eada54c276a7c3e85&url=https://translate.google.com/?text={get_key}').json()
    link_key = get_linkocto['shortenedUrl']
    for i in range(3, 0, -1):
        print(f'[LINK KEY: {link_key}\n')
        print(f'[DHP07][BẠN CÒN {i} LẦN NHẬP KEY]\n[VUI LÒNG NHẬP CHÍNH XÁC !]')
        enter_key = input('NHẬP KEY: ').lower()
        if enter_key in key:
            os.system("cls" if os.name == "nt" else "clear")
            print('[KEY ĐÚNG, ĐANG VÀO TOOL BY DHP07]')
            main()
        else:
            print('[KEY SAI HOẶC HẾT HẠN !]\n[VUI LÒNG LIÊN HỆ DHP07 !]\n')
            quit()
