import re, requests, time, os, random
from datetime import date, datetime
from pystyle import Write, Colors
from time import sleep
today = date.today()
count = 0

os.system('cls' if os.name == 'nt' else 'clear')
if __name__ == "__main__":
    listjob = []
    listck = []
    token_tds = Write.Input('Nhập Access_token TDS: ', Colors.green_to_yellow, interval=0.0001)
    info_tds = requests.get('https://traodoisub.com/api/?fields=profile&access_token=' + str(token_tds)).json()
    if 'success' in info_tds:
        user = info_tds['data']['user']
        xu = info_tds['data']['xu']
        xu_die = info_tds['data']['xudie']
        sleep(1)
        Write.Print(f'User: {user} | Coin: {xu} | Coin Die: {xu_die}\n', Colors.green_to_yellow, interval=0.0001)
        sleep(1.5)
    elif 'error' in info_tds:
        print(info_tds['error'])
        exit(1)
    Write.Print("""
        [1] - Like Sieu Re
        [2] - Cảm Xúc
        [3] - Follow
        [4] - Share
        [5] - Tham Gia Nhóm
        [X] - Chạy Random Job Thì Ngăn cách Bởi Dấu ' + '
        \n""", Colors.green_to_white, interval=0.0001)
    job = str(Write.Input('Nhập Job Cần Làm: ', Colors.green_to_white, interval=0.0001))
    dl1 = int(Write.Input('Nhập Delay Min: ', Colors.green_to_white, interval=0.0001))
    dl2 = int(Write.Input('Nhập Delay Max: ', Colors.green_to_white, interval=0.0002))
    chuyen = int(Write.Input('Sau Bao Nhiêu Job Thì Chuyển: ', Colors.green_to_white, interval=0.0002))
    delay = random.randint(dl1, dl2)
    for i in job.split('+'):
        if i == '1':listjob.append('like')
        elif i == '2':listjob.append('cx')
        elif i == '3':listjob.append('follow')
        elif i == '4':listjob.append('page')
        elif i == '5':listjob.append('share')
        elif i == '6':listjob.append('gr')
        else:Write.Print('Nhập Sai !', Colors.green_to_yellow, interval=0.0001);exit()
    for i in range(99999):
        ck = str(Write.Input(f'Nhập Cookie Thứ {i + 1}: ', Colors.green_to_yellow, interval=0.0001))
        if ck == "":break
        else:listck.append(ck)
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        for i in range(len(listck)):
            ck = listck[i]
            head = {
                'cookie': ck,
                'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
            }
            check = requests.get('https://mbasic.facebook.com/profile.php', headers=head).text
            if 'Đăng nhập Facebook để xem trang cá nhân.' in str(check):
                Write.Print('Cookie Die !', Colors.green_to_red, interval=0.0001)
                continue
            else:
                uid = ck.split('i_user=')[1].split(';')[0]
                user = check.split('<title>')[1].split('<')[0]
                run = requests.get(f'https://traodoisub.com/api/?fields=run&id={uid}&access_token={token_tds}').json()
                if 'success' in run:
                    Write.Print(run['data']["msg"] + f' <> Name: {user} <> Uid: {uid} <> Có {len(listck)} Cookie\n', Colors.green_to_red, interval=0.0001)
                else:
                    print(run['error'])
                    continue
            while count < chuyen:
                jc = random.choice(listjob)
                if jc == 'like':
                    try:
                        joblike = requests.get(f'https://traodoisub.com/api/?fields=likesieure&access_token={token_tds}').json()
                        if 'error' in joblike:continue
                        for job in joblike:
                            try:
                                id = job['id']
                                id2 = str(id).split('_')[1]
                                host = 'https://mbasic.facebook.com'
                                url = host + '/reactions/picker/?is_permalink=1&ft_id=' + str(id2)
                                head_job = {'cookie': ck}
                                a = requests.get(url, headers=head_job).text
                                b = re.findall('/ufi/reaction/?.*?"', a)
                                if not b:continue
                                c = b[0].replace('amp;', '').replace('"', '')
                                url = host + c
                                done = requests.get(url=url, headers=head_job)
                                get_xu = requests.get(f'https://traodoisub.com/api/coin/?type=LIKESIEURE&id={id}&access_token={token_tds}').json()
                                if str(get_xu['success']) == '200':
                                    count += 1
                                    timem = datetime.now().strftime("%H:%M:%S")
                                    xucong = str(get_xu['data']['msg'])
                                    xutong = str(get_xu['data']['xu'])
                                    Write.Print(f'| {count} | {timem} | LIKESIEURE | {id2} | {xucong} | {xutong} |\n', Colors.green_to_white, interval=0.0001)
                                    if count >= chuyen:
                                        break
                                for t in range(delay, 0, -1):
                                    Write.Print(f'Làm Job Tiếp Theo Sau {t} Giây \r', Colors.green_to_white, interval=0.0001)
                                    time.sleep(1)
                            except:pass
                    except:continue
                elif str(jc)=='cx':
                    try:
                        jobcx = requests.get(f'https://traodoisub.com/api/?fields=reaction&access_token={token_tds}').json()
                        if 'error' in jobcx:continue
                        for i in range(int(len(jobcx))):
                            try:
                                id = str(jobcx[i]['id'])
                                typee = str(jobcx[i]['type'])
                                headers = {
                                    'authority': 'mbasic.facebook.com',
                                    'scheme': 'https',
                                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                                    'cookie':ck,
                                    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                                    'sec-ch-ua-mobile': '?0',
                                    'sec-ch-ua-platform': '"Windows"',
                                    'sec-fetch-dest': 'document',
                                    'sec-fetch-mode': 'navigate',
                                    'sec-fetch-site': 'none',
                                    'sec-fetch-user': '?1',
                                    'upgrade-insecure-requests': '1',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                                }
                                url = f'https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={id}'
                                a = requests.get(url, headers=headers).text
                                b = re.findall('/ufi/reaction/?.*?"',a)
                                if b == []:continue
                                number = 1 if typee == "LOVE" else 2 if typee == "HAHA" else 3 if typee == "ANGRY" else 4 if typee == "WOW" else 5 if typee == "SAD" else 6 if typee == "CARE" else 7
                                cc = str(b[number]).replace('amp;','').replace('"','')
                                donecx = requests.get(f"https://mbasic.facebook.com{cc}",headers=headers)
                                sleep(1)
                                get_xu = requests.get(f'https://traodoisub.com/api/coin/?type={typee}&id={id}&access_token={token_tds}').json()
                                if str(get_xu['success'])=='200':
                                    count += 1
                                    timem = datetime.now().strftime("%H:%M:%S")
                                    xucong = str(get_xu['data']['msg'])
                                    xutong = str(get_xu['data']['xu'])
                                    Write.Print(f'| {count} | {timem} | {typee} | {id} | {xucong} | {xutong} |\n',Colors.green_to_white,interval=0.0001)
                                    if count >= chuyen:
                                        break
                                for i in range(delay,0,-1):
                                    Write.Print(f'Làm Job Tiếp Theo Sau {i} Giây \r',Colors.green_to_white,interval=0.0001)
                                    time.sleep(1)
                            except:pass
                    except:continue
                elif str(jc)=='follow':
                    try:
                        jobfollow = requests.get(f'https://traodoisub.com/api/?fields=follow&access_token={token_tds}').json()
                        if 'error' in jobfollow:continue
                        for i in range(int(len(jobfollow))):
                            try:
                                id = str(jobfollow[i]['id'])
                                host = 'https://mbasic.facebook.com/profile.php?id='
                                head_job = {'cookie':ck}
                                url = host+str(id)
                                a = requests.get(url=url, headers=head_job).text
                                b = re.findall('/a/subscribe.php?.*?"', a)
                                if b == []:continue
                                else:
                                    c = b[0].replace('amp;','').replace('"','')
                                    url = (host+c).replace('/profile.php?id=','')
                                    done = requests.get(url=url, headers=head_job)
                                get_xu = requests.get(f'https://traodoisub.com/api/coin/?type=follow&id={id}&access_token={token_tds}').json()
                                if str(get_xu['success'])=='200':
                                    count += 1
                                    timem = datetime.now().strftime("%H:%M:%S")
                                    xucong = str(get_xu['data']['msg'])
                                    xutong = str(get_xu['data']['xu'])
                                    Write.Print(f'| {count} | {timem} | FOLLOW | {id} | {xucong} | {xutong} |\n',Colors.green_to_white,interval=0.0001)
                                    if count >= chuyen:
                                        break
                                for i in range(delay,0,-1):
                                    Write.Print(f'Làm Job Tiếp Theo Sau {i} Giây \r',Colors.green_to_white,interval=0.0001)
                                    time.sleep(1)
                            except:pass
                    except:continue
                elif str(jc) == 'page':
                    try:
                        jobpage = requests.get(f'https://traodoisub.com/api/?fields=page&access_token={token_tds}').json()
                        if 'error' in jobpage:continue
                        for i in range(int(len(jobpage))):
                            try:
                                id = jobpage[i]['id']
                                host = 'https://mbasic.facebook.com/profile.php?id='
                                head_job = {'cookie':ck}
                                url = host+str(id)
                                a = requests.get(url=url, headers=head_job).text
                                b = re.findall('/a/page/join/?.*?"', a)
                                if b == []:continue
                                else:
                                    c = b[0].replace('amp;','').replace('"','')
                                    url = (host+c).replace('/profile.php?id=','')
                                    donelp = requests.get(url=url, headers=head_job)
                                    get_xu = requests.get(f'https://traodoisub.com/api/coin/?type=PAGE&id={id}&access_token={token_tds}').json()
                                if 'success' in get_xu:
                                    count += 1
                                    timem = datetime.now().strftime("%H:%M:%S")
                                    xucong = str(get_xu['data']['msg'])
                                    xutong = str(get_xu['data']['xu'])
                                    Write.Print(f'| {count} | {timem} | LIKEPAGE | {id} | {xucong} | {xutong} |\n',Colors.green_to_white,interval=0.005)
                                    if count >= chuyen:
                                        break
                                for i in range(delay,0,-1):
                                    Write.Print(f'Làm Job Tiếp Theo Sau {i} Giây \r',Colors.green_to_blue,interval=0.005)
                                    time.sleep(1)
                            except:pass
                    except:continue
                elif str(jc) == 'share':
                    try:
                        jobs = requests.get(f'https://traodoisub.com/api/?fields=share&access_token={token_tds}').json()
                        if 'error' in jobs:pass
                        for i in range(len(jobs)):
                            try:
                                id = jobs[i]['id']
                                host = 'https://mbasic.facebook.com/'
                                msg = ''
                                headers = {
                                    'authority': 'mbasic.facebook.com',
                                    'scheme': 'https',
                                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                                    'cookie':ck,
                                    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                                    'sec-ch-ua-mobile': '?0',
                                    'sec-ch-ua-platform': '"Windows"',
                                    'sec-fetch-dest': 'document',
                                    'sec-fetch-mode': 'navigate',
                                    'sec-fetch-site': 'none',
                                    'sec-fetch-user': '?1',
                                    'upgrade-insecure-requests': '1',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                                }
                                url = requests.get(host+id,headers=headers).url
                                share = requests.get(url,headers=headers).text
                                _find = re.findall('composer/mbasic/.*?"',share)
                                if _find == []:pass
                                else:
                                    data = _find[0].replace('amp;','').replace('"','')
                                    done1 = requests.get(host+data,headers=headers).text
                                    fb_dtsg = done1.split('name="fb_dtsg" value="')[1].split('"')[0]
                                    jazoest = done1.split('name="jazoest" value="')[1].split('"')[0]
                                    target = done1.split('name="target" value="')[1].split('"')[0]
                                    csid = done1.split('name="csid" value="')[1].split('"')[0]
                                    privacyx = done1.split('name="privacyx" value="')[1].split('"')[0]
                                    sid = done1.split('name="sid" value="')[1].split('"')[0]
                                    data = {
                                        "fb_dtsg": fb_dtsg,
                                        "jazoest": jazoest,
                                        "at": "",
                                        "target": target,
                                        "csid": csid,
                                        "c_src": "share",
                                        "referrer": "feed",
                                        "ctype": "advanced",
                                        "cver": "amber_share",
                                        "users_with": "",
                                        "album_id": "",
                                        "waterfall_source": "advanced_composer_timeline",
                                        "privacyx": privacyx,
                                        "appid": "0",
                                        "sid": sid,
                                        "linkUrl": "",
                                        "m": "self",
                                        "xc_message": msg,
                                        "view_post": "Chia sẻ",
                                        "shared_from_post_id": sid,
                                    }
                                    share2 = done1.split('action="/composer/mbasic/?csid=')[1].split('"')[0]
                                    share3 = share2.replace('amp;','')
                                    _share = requests.post(f'https://mbasic.facebook.com/composer/mbasic/?csid={share3}',headers=headers,data=data).text
                                get_xu = requests.get(f'https://traodoisub.com/api/coin/?type=SHARE&id={id}&access_token={token_tds}').json()
                                if 'success' in get_xu:
                                    count += 1
                                    timem = datetime.now().strftime("%H:%M:%S")
                                    xucong = str(get_xu['data']['msg'])
                                    xutong = str(get_xu['data']['xu'])
                                    Write.Print(f'| {count} | {timem} | SHARE | {id} | {xucong} | {xutong} |\n',Colors.green_to_white,interval=0.005)
                                    if count >= chuyen:
                                        break
                                for i in range(delay,0,-1):
                                    Write.Print(f'Làm Job Tiếp Theo Sau {i} Giây \r',Colors.green_to_blue,interval=0.005)
                                    time.sleep(1)
                            except:pass
                    except:pass
                elif str(jc) == 'gr':
                    try:
                        jobgr = requests.get(f'https://traodoisub.com/api/?fields=group&access_token={token_tds}').json()
                        if 'error' in jobgr:pass
                        for i in range(len(jobgr)):
                            try:
                                id = jobgr[i]['id']
                                headers = {
                                    'authority': 'mbasic.facebook.com',
                                    'scheme': 'https',
                                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                                    'cookie':ck,
                                    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                                    'sec-ch-ua-mobile': '?0',
                                    'sec-ch-ua-platform': '"Windows"',
                                    'sec-fetch-dest': 'document',
                                    'sec-fetch-mode': 'navigate',
                                    'sec-fetch-site': 'none',
                                    'sec-fetch-user': '?1',
                                    'upgrade-insecure-requests': '1',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                                }
                                url = requests.get(f'https://mbasic.facebook.com/{id}',headers=headers).url
                                step1 = requests.get(url,headers=headers).text
                                step2 = re.findall('/a/group/join/?.*?"',step1)
                                if step2 ==[]:pass
                                else:
                                    step3 = step2[0].replace('amp;','').replace('"','')
                                    fb_dtsg = step1.split('name="fb_dtsg" value="')[1].split('"')[0]
                                    jazoest = step1.split('name="jazoest" value="')[1].split('"')[0]
                                    _data = {"fb_dtsg": fb_dtsg,"jazoest": jazoest}
                                    _joingroup = requests.post(f'https://mbasic.facebook.com{step3}',headers=headers,data=_data).text
                                get_xu = requests.get(f'https://traodoisub.com/api/coin/?type=GROUP&id={id}&access_token={token_tds}').json()
                                if 'success' in get_xu:
                                    count += 1
                                    timem = datetime.now().strftime("%H:%M:%S")
                                    xucong = str(get_xu['data']['msg'])
                                    xutong = str(get_xu['data']['xu'])
                                    Write.Print(f'| {count} | {timem} | GROUP | {id} | {xucong} | {xutong} |\n',Colors.green_to_white,interval=0.005)
                                    if count >= chuyen:
                                        break
                                for i in range(delay,0,-1):
                                    Write.Print(f'Làm Job Tiếp Theo Sau {i} Giây \r',Colors.green_to_blue,interval=0.005)
                                    time.sleep(1)
                            except:pass
                    except:pass
