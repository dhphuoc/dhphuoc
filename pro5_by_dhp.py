import requests , time, os, random, re
from datetime import date, datetime
from time import sleep
today = date.today()
count = 0

os.system('cls' if os.name=='nt' else 'clear')
if __name__=="__main__":
    listjob = []
    listck = []
    token_tds = input('Nhập Access_token TDS: ')
    info_tds=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds)).json()
    if 'success' in info_tds:
        user=info_tds['data']['user']
        xu=info_tds['data']['xu']
        xu_die=info_tds['data']['xudie']
        sleep(1)
        print(f'User: {user} | Coin: {xu}')
        sleep(1.5)
    if 'error' in info_tds:
        print(info_tds['error'])
    print("""[1] - Like\n[2] - Tham Gia Nhóm\n[3] - Cảm Xúc\n[X] - Chạy Random Job Thì Ngăn cách Bởi Dấu ' + '""")
    job = str(input('Nhập Job Cần Làm: '))
    dl1 = int(input('Nhập Delay Min: '))
    dl2 = int(input('Nhập Delay Max: '))
    delay = random.randint(dl1,dl2)
    chuyen = int(input('Sau Bao Nhiêu Job Thì Chuyển: '))
    for i in job.split('+'):
        if i=='1':listjob.append('like')
        elif i=='2':listjob.append('gr')
        elif i=='3':listjob.append('camxuc')
        else:print('Nhập Sai !'),exit(0)
    for i in range(99999):
        ck = str(input(f'Nhập Cookie Pro5 Thứ {i+1}: '))
        if ck == "":
            break
        else:
            listck.append(ck)
    while (True):
        for i in range(len(listck)):
            cookie = listck[i]
            head = {
                'cookie' : cookie,
                'useragent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
                }
            check = requests.get('https://mbasic.facebook.com/profile.php', headers=head).text
            if 'Đăng nhập Facebook để xem trang cá nhân.' in str(check):
                print('Cookie Die !')
                continue
            else:
                uid = cookie.split('i_user=')[1].split(';')[0]
                user = check.split('<title>')[1].split('<')[0]
                run = requests.get(f'https://traodoisub.com/api/?fields=run&id={uid}&access_token={token_tds}').json()
                s=0
                if 'success' in run:
                    os.system('cls' if os.name=='nt' else 'clear')
                    print(run['data']["msg"]+f' <> Name: {user} <> Uid: {uid}')
                else:
                    print(run['error']);continue
            while (True):
                jc = random.choice(listjob)
                if str(jc)=='like':
                    try:
                        joblike = requests.get(f'https://traodoisub.com/api/?fields=likesieure&access_token={token_tds}').json()
                        if 'error' in joblike:continue
                        for i in range(int(len(joblike))):
                            try:
                                id = joblike[i]['id']
                                id2 = str(id).split('_')[1]
                                host = 'https://mbasic.facebook.com'
                                url = host+'/reactions/picker/?is_permalink=1&ft_id='+str(id2)
                                head_job = {'cookie': cookie}
                                a = requests.get(url, headers=head_job).text
                                b = re.findall('/ufi/reaction/?.*?"',a)
                                if b == []:continue
                                else:
                                    c = b[0].replace('amp;','').replace('"','')
                                    url = host+c
                                    done = requests.get(url=url, headers=head_job)
                                get_xu = requests.get(f'https://traodoisub.com/api/coin/?type=LIKESIEURE&id={id}&access_token={token_tds}').json()
                                print(get_xu)
                                if str(get_xu['success'])=='200':
                                    count += 1
                                    timem = datetime.now().strftime("%H:%M:%S")
                                    xucong = str(get_xu['data']['msg'])
                                    xutong = str(get_xu['data']['xu'])
                                    print(f'| {count} | {timem} | LIKESIEURE | {id2} | {xucong} | {xutong} |')
                                    if count > 0 and count % chuyen == 0:
                                        break
                                else:
                                    print(f'| X | {timem} | LIKESIEURE | {id2} | {xutong} |', end='\r')
                                for i in range(delay,0,-1):
                                    print(f'Làm Job Tiếp Theo Sau {i} Giây', end='\r')
                                    time.sleep(1)
                            except:pass
                    except:continue
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
                                    'cookie': cookie,
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
                                    print(f'| {count} | {timem} | GROUP | {id} | {xucong} | {xutong} |')
                                    if count > 0 and count % chuyen == 0:
                                        continue
                                else:
                                    print(f'| X | {timem} | GROUP | {id} | {xutong} |', end='\r')
                                for i in range(delay,0,-1):
                                    print(f'Làm Job Tiếp Theo Sau {i} Giây', end='\r')
                                    time.sleep(1)
                            except:pass
                    except:pass  
                elif str(jc)=='camxuc':
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
                                    print(f'| {count} | {timem} | {typee} | {id} | {xucong} | {xutong} |')
                                    if count > 0 and count % chuyen == 0:
                                        continue
                                else:
                                    print(f'| X | {timem} | {typee} | {id} | {xutong} |', end='\r')
                                for i in range(delay,0,-1):
                                    print(f'Làm Job Tiếp Theo Sau {i} Giây', end='\r')
                                    time.sleep(1)
                            except:pass
                    except:continue
