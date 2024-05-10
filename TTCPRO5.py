import requests, uuid, sys, os, time, json, base64
from time import sleep
from datetime import datetime
listuid = []
listcookie = []

class ApiTTC(object):
	def Type(self, type_1) :
		if type_1 == "LOVE" :
			type_2 = '1678524932434102'
		elif type_1 == "CARE" :
			type_2 = '613557422527858'
		elif type_1 == "WOW" :
			type_2 = '478547315650144'
		elif type_1 == "HAHA" :
			type_2 = '115940658764963'
		elif type_1 == "SAD" :
			type_2 = '908563459236466'
		elif type_1 == "ANGRY" :
			type_2 = '444813342392137'
		return type_2
	
	def NhiemVu(self, So, ttt) :
		if ttt == 3 :
			ttt -= 3
		if So == 1 :
			loai = "/subcheo/"
		elif So == 2 :
			loai = "/camxuccheo/"
		elif So == 3 :
			loai = "/thamgianhomcheo/"
		else :
			type_5 = ['/subcheo/','/camxuccheo/','/thamgianhomcheo/']
			loai = type_5[ttt]
		return loai
	
	def CauHinh(self, id, cookie,name):
		url = 'https://tuongtaccheo.com/cauhinh/datnick.php'
		data = f'iddat%5B%5D={id}&loai=fb'
		self.headers ={
			'Host':'tuongtaccheo.com',
			'accept':'*/*',
			'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36',
			'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
			'cookie':f'{cookie}'
		}
		ve = requests.post(url= url, headers= self.headers , data= data).text
		if ve == '1' :
			print (f'CẤU HÌNH THÀNH CÔNG! UID: {id} | NAME: {name}')
		else :
			print (f'BẠN CHƯA THÊM UID: {id} VÀO CẤU HÌNH!')
			exit()
	
	def GetNV(self, Type, cookie):
		self.headers = {
			'Host':'tuongtaccheo.com',
			'accept':'application/json, text/javascript, */*; q=0.01',
			'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36',
			'cookie':f'{cookie}',
			'x-requested-with':'XMLHttpRequest'
		}
		get_nv = requests.get(f'https://tuongtaccheo.com/kiemtien{Type}getpost.php',headers=self.headers)
		return get_nv
	
	def NhanXu(self, cookie, Type, data) :
		url = f'https://tuongtaccheo.com/kiemtien{Type}nhantien.php'
		self.headers = {
			'Host':'tuongtaccheo.com',
			'accept':'*/*',
			'x-requested-with':'XMLHttpRequest',
			'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36',
			'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
			'referer':f'https://tuongtaccheo.com/kiemtien{Type}',
			'cookie':f'{cookie}'
		}
		nhan = requests.post(url=url, headers=self.headers, data=data)
		return nhan
	
	def LoginTTC(self, token) :
		data = {
			'access_token': token
		}
		text_1 = requests.post("https://tuongtaccheo.com/logintoken.php",data=data)
		log = text_1.json()["status"]
		if log == "success" :
			xu = text_1.json()["data"]["sodu"]
			name = text_1.json()["data"]["user"]
			print ('LOGIN THÀNH CÔNG!',end='\r')
			print (f'NAME: {name} | COIN: {xu} | TOOL AUTO TTC | BY: DHP07')
			cookie = text_1.headers["Set-Cookie"]
		else :
			print ('Đăng Nhập Thất Bại ')
			exit()
		return cookie
	
	def InfoTTC(self, cookie) :
		self.headers = {
			'Host':'tuongtaccheo.com',
			'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36',
			'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
			'cookie':cookie
		}
		response = requests.get('https://tuongtaccheo.com/home.php',headers=self.headers).text
		xu = response.split('<li><a>Số dư: <strong style="color: red;" id="soduchinh">')[1].split('<')[0]
		return xu
	
class Fuoc(object):
	def Logo(self):
		FUOC = '[COPYRIGHT: ĐÀM HỮU PHƯỚC  - DHP07]\n[DHP07 TOOL   -   ZALO: 0862964954]\n[MOMO: 0862964954 - MB: 0862964954]\n'
		os.system("cls" if os.name == "nt" else "clear")
		print(FUOC)
	
	def delay(self, value):
		while(value>1):
			value-=0.1
			print(F'[DHP07][DELAY][X    ][{str(value)[0:5]}]', '               ', end='\r'); time.sleep(1/50)
			print(F'[DHP07][DELAY][ X   ][{str(value)[0:5]}]', '               ', end='\r'); time.sleep(1/50)
			print(F'[DHP07][DELAY][  X  ][{str(value)[0:5]}]', '               ', end='\r'); time.sleep(1/50)
			print(F'[DHP07][DELAY][   X ][{str(value)[0:5]}]', '               ', end='\r'); time.sleep(1/50)
			print(F'[DHP07][DELAY][    X][{str(value)[0:5]}]', '               ', end='\r'); time.sleep(1/50)

class ApiPro5:
	def __init__(self, cookies,fb_dtsg,jazoet,id_page) -> None:
		self.headers = {
			'authority': 'www.facebook.com',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'vi',
			'cookie': cookies,
			'sec-ch-prefers-color-scheme': 'light',
			'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
			'viewport-width': '1366',
		}
		url_profile = requests.get('https://www.facebook.com/me', headers=self.headers).url
		profile = requests.get(url_profile, headers=self.headers).text
		self.fb_dtsg = fb_dtsg
		self.jazoet = jazoet
		self.user_id = id_page

	def ThamGiaGroup(self, group_id):
		data = {
			'fb_dtsg': self.fb_dtsg,
			'jazoest': self.jazoet,
			'fb_api_caller_class': 'RelayModern',
			'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
			'variables': '{"feedType":"DISCUSSION","groupID":"'+group_id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUPS_ENGAGE_TAB","attribution_id_v2":"GroupsCometCrossGroupFeedRoot.react,comet.groups.feed,tap_tabbar,1667116100089,433821,2361831622,","group_id":"'+group_id+'","group_share_tracking_params":null,"actor_id":"'+self.user_id+'","client_mutation_id":"2"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":false,"scale":1,"source":"GROUPS_ENGAGE_TAB","renderLocation":"group_mall","__relay_internal__pv__GlobalPanelEnabledrelayprovider":false,"__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true}',
			'server_timestamps': 'true',
			'doc_id': '5915153095183264',
		}
		response = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
		return response

	def CamXuc(self, id_post, reaction):
		try:
			url = requests.get('https://www.facebook.com/'+id_post, headers=self.headers).url
			home = requests.get(url, headers=self.headers).text
			feedback_id = home.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
			data = {
				'fb_dtsg': self.fb_dtsg,
				'jazoest': self.jazoet,
				'fb_api_caller_class': 'RelayModern',
				'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
				'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667106623951,429237,190055527696468,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+reaction+'","feedback_source":"PROFILE","is_tracking_encrypted":true,"tracking":["AZXg8_yM_zhwrTY7oSTw1K93G-sycXrSreRnRk66aBJ9mWkbSuyIgNqL0zHEY_XgxepV1XWYkuv2C5PuM14WXUB9NGsSO8pPe8qDZbqCw5FLQlsGTnh5w9IyC_JmDiRKOVh4gWEJKaTdTOYlGT7k5vUcSrvUk7lJ-DXs3YZsw994NV2tRrv_zq1SuYfVKqDboaAFSD0a9FKPiFbJLSfhJbi6ti2CaCYLBWc_UgRsK1iRcLTZQhV3QLYfYOLxcKw4s2b1GeSr-JWpxu1acVX_G8d_lGbvkYimd3_kdh1waZzVW333356_JAEiUMU_nmg7gd7RxDv72EkiAxPM6BA-ClqDcJ_krJ_Cg-qdhGiPa_oFTkGMzSh8VnMaeMPmLh6lULnJwvpJL_4E3PBTHk3tIcMXbSPo05m4q_Xn9ijOuB5-KB5_9ftPLc3RS3C24_7Z2bg4DfhaM4fHYC1sg3oFFsRfPVf-0k27EDJM0HZ5tszMHQ"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":1}',
				'server_timestamps': 'true',
				'doc_id': '5703418209680126',
			}
			reaction = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
			return {'status': True, 'url': url}
		except:
			return {'status': False, 'url': url}
		
	def TheoDoi(self, uid):
		data = {
			'fb_dtsg': self.fb_dtsg,
			'jazoest': self.jazoet,
			'fb_api_caller_class': 'RelayModern',
			'fb_api_req_friendly_name': 'CometUserFollowMutation',
			'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667114418950,431532,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+uid+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":1}',
			'server_timestamps': 'true',
			'doc_id': '5032256523527306',
		}
		subscribe = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
		return subscribe

def InfoFB(cookie):
	headers = {
		'authority': 'mbasic.facebook.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'en-US,en;q=0.9',
		'cache-control': 'max-age=0',
		'cookie': cookie,
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
	jazoet = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
	return json.dumps({'fb_dtsg':fb_dtsg,'jazoet':jazoet})

def GetPage(cookie):
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
		return a
def PageRun(page_index):
    id_page = get_tt_page[page_index - 1]['profile']['id']
    name = get_tt_page[page_index - 1]['profile']['name']
    ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
    print('='*60)
    print(f'[DHP07] ĐANG CHẠY UID: {id_page} | NAME: {name}')
    print('='*60)
    ApiTTC().CauHinh(id_page, cookie_ttc, name)
    data = InfoFB(cookie)
    fb_dtsg = json.loads(data)['fb_dtsg']
    jazoet = json.loads(data)['jazoet']
    return ApiPro5(cookies=ck_pro5, fb_dtsg=fb_dtsg, jazoet=jazoet,id_page=id_page)
Fuoc().Logo()
token = input('NHẬP ACCESS_TOKEN TTC: ')
print('='*60)
cookie_ttc = ApiTTC().LoginTTC(token)
print('='*60)
cookie = input('NHẬP COOKIE FACEBOOK: ')
Fuoc().Logo()
get_tt_page = GetPage(cookie)
print('='*60)
for idx, page in enumerate(get_tt_page, 1):
	print(f'[{idx}] UID: {page["profile"]["id"]} | NAME: {page["profile"]["name"]}')
selected_pages = input('BẠN MUỐN CHẠY PAGE SỐ MẤY (NHIỀU PAGE: 1+2+3): ').split('+')
selected_pages = [int(x.strip()) for x in selected_pages]
pages_info = []
delay = float(input('NHẬP DELAY: '))
print('='*60)
print(f'[1] FOLLOW [2] REACTION [3] GROUP [4] RANDOM')
so = int(input('NHẬP NHIỆM VỤ: '))
print('='*60)
Fuoc().Logo()
print('='*60)
ApiTTC().LoginTTC(token) 
print('='*60)
for page_index in selected_pages:
    page_info = {}
    page_info['id'] = get_tt_page[page_index - 1]['profile']['id']
    page_info['name'] = get_tt_page[page_index - 1]['profile']['name']
    pages_info.append(page_info)

for page_info in pages_info:
    id_page = page_info['id']
    name = page_info['name']
    ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
    print('='*60)
    print(f'[DHP07] ĐANG CHẠY UID: {id_page} | NAME: {name}')
    print('='*60)
    ApiTTC().CauHinh(id_page, cookie_ttc, name)
    data = InfoFB(cookie)
    fb_dtsg = json.loads(data)['fb_dtsg']
    jazoet = json.loads(data)['jazoet']
    fb = ApiPro5(cookies=ck_pro5, fb_dtsg=fb_dtsg, jazoet=jazoet,id_page=id_page)
    total = 0
    ttt = 0
    while True:
        loai = ApiTTC().NhiemVu(so, ttt) 
        ttt+= 1
        print("ĐANG TÌM NHIỆM VỤ",end="\r")
        if loai == "/subcheo/":
            list_job = ApiTTC().GetNV(loai,cookie_ttc)
            b = list_job.text
            a = list_job.json()
            if b == "[]":
                print("KHÔNG TÌM THẤY NHIỆM VỤ FOLLOW",end="\r")
            else:
                for list_job_ in a:
                    id_job = list_job_["idpost"]
                    fb.TheoDoi(id_job)
                    data = f'id={id_job}'
                    nhan = ApiTTC().NhanXu(cookie_ttc,loai,data).json()
                    xu_1 = ApiTTC().InfoTTC(cookie_ttc) 
                    try:
                        a = nhan["error"]
                        print(f'[DHP07][X][{datetime.now().strftime("%H:%M:%S")}][FOLLOW][FAILURE!]', end='\r')
                    except:
                        total += 1
                        print(f'[DHP07][{total}][{datetime.now().strftime("%H:%M:%S")}][FOLLOW][+700][{xu_1}]')
                        Fuoc().delay(delay)
                        if total >= 10:
                            page_index += 1
                            if page_index > len(selected_pages):
                                page_index = 1
                            fb = PageRun(page_index)
                            total = 0
        elif loai == "/thamgianhomcheo/":
            list_job = ApiTTC().GetNV(loai, cookie_ttc)
            b = list_job.text
            a = list_job.json()
            if b == "[]":
                print("KHÔNG TÌM THẤY NHIỆM VỤ GROUP", end="\r")
            else:
                for list_job_ in a:
                    id_job = list_job_["idpost"]
                    lam = fb.ThamGiaGroup(id_job)
                    data = f"id={id_job}"
                    nhan = ApiTTC().NhanXu(cookie_ttc, loai, data)
                    nhan_2 = nhan.json()
                    xu_1 = ApiTTC().InfoTTC(cookie_ttc)
                    try:
                        a = nhan_2["error"]
                        print(f'[DHP07][X][{datetime.now().strftime("%H:%M:%S")}][GROUP][FAILURE!]', end='\r')
                    except:
                        total += 1
                        print(f'[DHP07][{total}][{datetime.now().strftime("%H:%M:%S")}][GROUP][+1200][{xu_1}]')
                        Fuoc().delay(delay)
                    if total >= 10:
                        page_index += 1
                        if page_index > len(selected_pages):
                            page_index = 1
                        fb = PageRun(page_index)
                        total = 0
        elif loai == "/camxuccheo/":
            list_job = ApiTTC().GetNV(loai, cookie_ttc)
            b = list_job.text
            a = list_job.json()
            if b == "[]":
                print("KHÔNG TÌM THẤY NHIỆM VỤ CẢM XÚC", end="\r")
            else:
                for list_job_ in a:
                    id_job = list_job_["idpost"]
                    type_1 = list_job_["loaicx"]
                    type_2 = ApiTTC().Type(type_1)
                    lam = fb.CamXuc(id_job, type_2)
                    data = f"id={id_job}&loaicx={type_1}"
                    nhan = ApiTTC().NhanXu(cookie_ttc, loai, data)
                    nhan_2 = nhan.json()
                    xu_1 = ApiTTC().InfoTTC(cookie_ttc)
                    try:
                        a = nhan_2["error"]
                        print(f'[DHP07][X][{datetime.now().strftime("%H:%M:%S")}][{type_1}][FAILURE!]', end='\r')
                    except:
                        total += 1
                        print(f'[DHP07][{total}][{datetime.now().strftime("%H:%M:%S")}][{type_1}][+700][{xu_1}]')
                        Fuoc().delay(delay)
                    if total >= 10:
                        page_index += 1
                        if page_index > len(selected_pages):
                            page_index = 1
                        fb = PageRun(page_index)
                        total = 0