import requests
from time import sleep

cookie = input(f'NHẬP COOKIE FACEBOOK: ')
headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    'cache-control': 'max-age=0',
    'cookie': cookie,
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
response = requests.get('https://mbasic.facebook.com/',headers=headers).text
fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
jazoest = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
idpef = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data={'fb_dtsg': fb_dtsg,'jazoest': jazoest,'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}','doc_id': '5300338636681652'}).json()
a = idpef['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
sl = 0
for b in a:
    sl +=1
    uid = b['profile']['id']
    name = b['profile']['name']
    delegate_page_id = b['profile']['delegate_page_id']
    ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],uid)
    print(ck_pro5)
    open('cookie.txt', "a+").write(f'{ck_pro5}\n')
    sleep(1)
