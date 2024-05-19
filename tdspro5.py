import requests, random
from time import sleep
count = 0;sonvlam = 0;s = 0;dem = 0;luot = 0
TOKEN = []
UID = []
tokentds = input('NHẬP ACCESS_TOKEN TDS: ')
sopage = int(input('BẠN MUỐN CHẠY BAO NHIỀU PAGE: '))
for i in range(sopage):
    luot+=1
    token = input(f"NHẬP TOKEN PAGE THỨ {luot}: ")
    TOKEN.append({'token': token})
    uid = input(f"NHẬP UID PAGE THỨ {luot}: ")
    UID.append({'uid': uid})
delay = int(input('NHẬP DELAY: '))
print('| 1 <> LIKE | 2 <> FOLLOW |')
chon = input('CHỌN NHIỆM VỤ: ')
class Api:
    def __init__(self, token):
        self.token = token
    def Follow (self, idnv):
        fl = requests.post(f'https://graph.facebook.com/{idnv}/subscribers?access_token={self.token}')
        if fl.text=='true':pass
    def Like(self, idnv):
        urllike = 'https://graph.facebook.com/'+str(idnv)+'/likes'
        datalike = 'access_token='+str(self.token)
        like = requests.post(urllike, data=datalike)
        if like.text=='true':pass
def datcauhinh(uid):
    res = requests.get(f"https://traodoisub.com/api/?fields=run&id={uid}&access_token={tokentds}").json()
    if 'success' in res:
        print(f'ĐANG CẤU HÌNH UID: {uid} | TRẠNG THÁI: THÀNH CÔNG')
    else:
        print(f'BẠN CHƯA THÊM UID: {uid} VÔ TDS')
        quit()
def nhanxu(dem,type,idnv,tokentds):
    nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={idnv}&access_token={tokentds}').json()
    if 'success' in nhan:
        xu = nhan['data']['xu'];idn = nhan['data']['id'];msg = nhan['data']['msg']
        print(f'| {dem} | {idn} | {msg} | {xu} |')
    else:
        print(f'| X | BẠN CHƯA LÀM NHIỆM VỤ', end='\r')
if chon == '1':
    for tokens, ids in zip(TOKEN, UID):
        token = tokens['token'].strip("\n")
        uid = ids['uid'].strip("\n")
        print(f'ĐANG CHẠY UID: {uid}')
        api = Api(token)
        datcauhinh(uid)
        while(True):
            listlike=requests.get('https://traodoisub.com/api/?fields=likesieure&access_token='+str(tokentds))
            if 'id' in listlike.text:break
        snv=len(listlike.json())
        s=s+snv
        tsnv=s
        print(f'TÌM THẤY {str(snv)} NHIỆM VỤ LIKE')
        for i in range(0,len(listlike.json()),1):
            idnv = listlike.json()[i]['id']
            likes = api.Like(idnv)
            type = 'LIKESIEURE'
            dem+=1
            nhanx = nhanxu(dem, type, idnv, tokentds)
            for x in range(delay, -1, -1):
                print(f'[DELAY][X    ][{x}]','     ',end='\r');sleep(1/6)
                print(f'[DELAY][ X   ][{x}]','     ',end='\r');sleep(1/6)
                print(f'[DELAY][  X  ][{x}]','     ',end='\r');sleep(1/6)
                print(f'[DELAY][   X ][{x}]','     ',end='\r');sleep(1/6)
                print(f'[DELAY][    X][{x}]','     ',end='\r');sleep(1/6)
            if likes == True:
                sonvlam += 1
            if count == 10:
                continue
elif chon == '2':
    for tokens, ids in zip(TOKEN, UID):
        token = tokens['token'].strip("\n")
        uid = ids['uid'].strip("\n")
        print(f'ĐANG CHẠY UID: {uid}')
        api = Api(token)
        datcauhinh(uid)
        while(True):
            listfollow=requests.get(f'https://traodoisub.com/api/?fields=follow&access_token='+str(tokentds))
            if 'id' in listfollow.text:break
        snv=len(listfollow.json())
        s=s+snv
        tsnv=s
        print(f'TÌM THẤY {str(snv)} NHIỆM VỤ FOLLOW')
        for i in range(0,len(listfollow.json()),1):
            idnv = listfollow.json()[i]['id']
            fl = api.Follow(idnv)
            type = 'FOLLOW'
            dem+=1
            nhanx = nhanxu(dem, type, idnv, tokentds)
            for x in range(delay, -1, -1):
                print(f'[DELAY][X    ][{x}]','     ',end='\r');sleep(1/6)
                print(f'[DELAY][ X   ][{x}]','     ',end='\r');sleep(1/6)
                print(f'[DELAY][  X  ][{x}]','     ',end='\r');sleep(1/6)
                print(f'[DELAY][   X ][{x}]','     ',end='\r');sleep(1/6)
                print(f'[DELAY][    X][{x}]','     ',end='\r');sleep(1/6)
            if fl == True:
                sonvlam += 1
            if count == 10:
                continue
