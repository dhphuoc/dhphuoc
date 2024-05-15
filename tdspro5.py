import requests, random
from time import sleep
count = 0
sonvlam = 0
s = 0
TOKEN = [
     {'token':''},
     {'token':''}, 
     {'token':''},
     {'token':''},
]
UID = [
     {'uid':''},
     {'uid':''}, 
     {'uid':''},
     {'uid':''},
]
tokentds = input('NHẬP TOKEN TDS: ')
print('1 <> LIKE | 2 <> FOLLOW | 3 <> REACTION(COMING SOON) | 4 <> SHARE(COMING SOON) | 5 <> COMENT(COMING SOON) | 6 <> JOIN GROUP(COMING SOON) |')
chon = input('CHỌN NHIỆM VỤ: ')
class Api:
    def __init__(self, token):
        self.token = token
    def Follow (self, idnv):
        fl = requests.post(f'https://graph.facebook.com/{idnv}/subscribers?access_token={self.token}')
        if fl.text=='true':
            print('THEO DÕI THÀNH CÔNG!!!')
        else:
            print('THEO DÕI THẤT BẠI!!!')
    def Like(self, idnv):
        urllike = 'https://graph.facebook.com/'+str(idnv)+'/likes'
        datalike = 'access_token='+str(self.token)
        like = requests.post(urllike, data=datalike)
        if like.text=='true':
            print('LIKE THÀNH CÔNG!!!')
        else:
            print('LIKE THẤT BẠI!!!')
    def Share(self, idnv):
        share=requests.post(f'https://graph.facebook.com/me/feed?method=POST&link=https://www.facebook.com/{idnv}&access_token={self.token}')
        if share.json()=='true':
            print('SHARE THÀNH CÔNG!!!')
        else:
            print('SHARE THẤT BẠI!!!')
    def Reaction(self, type_post, idnv):
        # if str(type_post) == 'LIKE':
        #         type_rect = 'LIKE'
        #         v = 1
        # elif str(type_post) == 'LOVE':
        #         type_rect = 'LOVE '
        #         v = 2
        # elif str(type_post) == 'CARE':
        #         type_rect = 'CARE '
        #         v = 3
        # elif str(type_post) == 'HAHA':
        #         type_rect = 'HAHA '
        #         v = 4
        # elif str(type_post) == 'WOW':
        #         type_rect = 'WOW  '
        #         v = 5
        # elif str(type_post) == 'SAD':
        #         type_rect = 'SAD  '
        #         v = 6
        # elif str(type_post) == 'ANGRY':
        #         type_rect = 'ANGRY'
        #         v = 7
        reac = requests.post(f'https://graph.facebook.com/{idnv}/reactions?type={type_post}&access_token={self.token}')
        if reac.json()=='true':
            print(f'{type} THÀNH CÔNG!!!')
        else:
            print(f'{type} THẤT BẠI!!!')
def datcauhinh(uid):
    res = requests.get(f"https://traodoisub.com/api/?fields=run&id={uid}&access_token={tokentds}").json()
    print(res)
def nhanxu(type,idnv,tokentds):
    nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={idnv}&access_token={tokentds}').json()
    print(nhan)
while True:
   for tokens, ids in zip(TOKEN, UID):
        token = tokens['token'].strip("\n")
        uid = ids['uid'].strip("\n")
        print(f'ĐANG CHẠY UID: {uid}')
        api = Api(token)
        datcauhinh(uid)
        while(True):
            if chon == '1':
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
                    sleep(20)
                    type = 'LIKESIEURE'
                    nhanx = nhanxu(type, idnv, tokentds)
                    if likes == True:
                        sonvlam += 1
                    if count == 10:
                        continue
            elif chon == '2':
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
                    sleep(50)
                    type = 'FOLLOW'
                    nhanx = nhanxu(type, idnv, tokentds)
                    if fl == True:
                        sonvlam += 1
                    if count == 10:
                        continue
