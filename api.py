import requests, json
import uuid, re
from bs4 import BeautifulSoup
class Facebook_Api(object):
	def __init__(self, cookie):
		self.cookie = cookie
		self.headers = {'authority': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-language': 'en-US,en;q=0.9','cookie': cookie}
	
	def get_thongtin(self):
		try:
			home = requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).text
			self.fb_dtsg = home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
			self.jazoest = home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
			ten = home.split('<title>')[1].split('</title>')[0]
			self.user_id = self.cookie.split('c_user=')[1].split(';')[0]
			return ten, self.user_id
		except:
			return 0

	def follow(self, id):
		data = {'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHxqUW13xt0mUyEqxenFwLBwopU98nwgU765QdwSxucyU8EW1twYwJyEiwsobo6u3y4o11U2nwb-q7oc81xoswIK1Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61uwZwlo5qfK0zEkxe2GewyDwsoqBwJK2W5olwUwgojUlDw-wSU72m7-8wywdG7FobpEbUGdwb6223908O3216AzUjwTwNxe6Uak1xwJwxw','__csr':'hcp2vsTfcyBblX4JmmZOiFYKx7KWi_qT9jkxbOfKAAlXWmHGGlq8kNsOVanp9WDQKEHXKRWGulGhaAHHy8VeiWGuUGVoyQUFaui54cCHpp-WCxqHyV9qyUx153qzoWE8ql3pEG4p8pyVGCyooCxe5ojBy98aHG4Eb8mG269Vby8be4oGUO9whXxa2q2q49okyoy26q1BwYxe4E6W10y88E467Erzo6-2y5Etxl3UO2GWwaeu3-7o7uaw922t08K026O03iuC04f802PRw4bw2v80za0G80B-0b-e09dBw0Uww2DOw0jP80n7g3Iw1k208bzE1lU8E','__req':'5','__hs':'9362.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'GOOD','__rev':'1006788684','__s':'p2x8mf:qj6dvy:bj8e46','__hsi':'7185171904183015509','__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'lsd':'afdisHHGuglOo_hNSDt3Fb','__aaid':'775223720487728','__spin_r':'1006788684','__spin_b':'trunk','__spin_t':'1672928199','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUserFollowMutation','variables':'{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1672928202199,140922,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+id+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":2}','server_timestamps':'true','doc_id':'5032256523527306',}
		headers = {"Host": "www.facebook.com","sec-ch-ua": "\"Chromium\";v\u003d\"107\", \"Not\u003dA?Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","viewport-width": "980","content-type": "application/x-www-form-urlencoded","x-fb-lsd": "afdisHHGuglOo_hNSDt3Fb","x-fb-friendly-name": "CometUserFollowMutation","sec-ch-prefers-color-scheme": "dark","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://www.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.facebook.com/"+id,"accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5","cookie":self.cookie}
		try:
			fl = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data)
			if 'IS_SUBSCRIBED' in fl.text:
				return True
			else:
				return fl
		except:
			return False 
	
	def page(self,id):
		data = {'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwAyU8EW0CEboG4E762S1DwUx60gu0BU2_CxS320om78bbwto88422y11xmfz83WwgEcHzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK0zEkxe2GewGwkUtxGm2SUbElxm3y11xfxmu3W2i4U72m7-8wywfCm2Sq2-azo2NwwwOg2cwMwhF8-4UdUcojxK2B0oobo8o','__csr':'g8JNc9n2tWr5W4til-I_On8J9rshlR8nZFiELH_Hnij4JfOJLOGiLoxLBlGRuZaGF4CZddQ4L_JfCiDKWVryuiqqFAcy8x6CBtqJkF8ZVExauAbgOtLAG5FUGFptxqfxi4Hzaz8CQ2SaxC9xCi48Wqqq11g8EaoS9g9U4m224oG68sGucx68wyg6G22mfxa4Xxq7EKbwi82LwNxu48c814EC2K3O5U-2WEhCxO1EwioeUiwiE6e3HwTw18C02k-0exw0deO0jV05Swe20bTw5_w1zF03I202po6e07Co0K6Zlw0jjo0E-0qW08ug8UhBw21e0fLw5Ww9K0Z86u','__req':'o','__hs':'19363.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'GOOD','__rev':'1006793331','__s':'v80lqo:poayhk:qxdcmk','__hsi':'7185553908092803679','__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'lsd':'V64c7kKr5hAtzX2IIDgKp8','__aaid':'775223720487728','__spin_r':'1006793331','__spin_b':'trunk','__spin_t':'1673017141','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometPageLikeCommitMutation','variables':'{"input":{"attribution_id_v2":"CometSinglePageHomeRoot.react,comet.page,via_cold_start,1673017144344,576155,250100865708545,","is_tracking_encrypted":true,"page_id":"'+id+'","source":"unknown","tracking":[],"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"isAdminView":false}','server_timestamps':'true','doc_id':'5491200487600992',}
		headers = {"Host": "www.facebook.com","sec-ch-ua": "\"Chromium\";v\u003d\"107\", \"Not\u003dA?Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","viewport-width": "980","content-type": "application/x-www-form-urlencoded","x-fb-lsd": "V64c7kKr5hAtzX2IIDgKp8","x-fb-friendly-name": "CometPageLikeCommitMutation","sec-ch-prefers-color-scheme": "dark","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://www.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.facebook.com/"+id,"accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5","cookie":self.cookie}
		try:
			page = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data)
			if 'FOLLOW' in page.text:
				return True
			else:
				return page.text
		except:
			return False
	
	def group(self, id):
			headers = {"Host": "www.facebook.com","sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36","viewport-width": "980","content-type": "application/x-www-form-urlencoded","x-fb-lsd": "gKT7R4dxIBjI4wUDUP5ivT","x-fb-friendly-name": "GroupCometJoinForumMutation","sec-ch-prefers-color-scheme": "dark","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://www.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.facebook.com/groups/"+id+"/","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5","cookie":self.cookie}
			data = {'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHJ16U9ob8ng5K8G6EjBWo2nDwAxu13wsongS3q2ibwyzE2qwJyEiwsobo6u3y4o2Gwfi0LVEtwMw65xO321Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-U2exi4UaEW2G1jxS6FobrwKxm5oe8464-5pUfEe88o4Wm7-8xmcwfCm2CVEbUGdG1Fwh888cA0z8c84qifxe3u364UrwFg662S26','__csr':'gadNAIYllhsKOE8IpidFPhcIx34Omy9-O9OO8hZ_8-kAymHGAybJqGlvmWl7nWBWJ7GqaXHz7GFe9oy_KBl7h6h4KVah94QeKVHACDyryqKdF5GuXXBCgNpbJ5jjGm8yQEWrCixl6xWuiih5yo-8wAy84mq4poN0Vzbxe16whAufgO5U8UKi4Eyu4EjwGK78527o8411wgocU5u1MwSwFyU8Uf8igaElw8e9xK2GewNgy5o5m1nDwLwrokm16www8G03cy0arw0Zyw0aaC0mG0eJzl8ow2Jw6tw44w4uzo045W1UgSeg0z-07X81-E0cNo0By1Wwi8fE0lYw2h81a8gw9u','__req':'k','__hs':'19363.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'EXCELLENT','__rev':'1006794317','__s':'gtlvj8:fxbzro:f2kk19','__hsi':'7185658639628512803','__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'lsd':'gKT7R4dxIBjI4wUDUP5ivT','__aaid':'1576489885859472','__spin_r':'1006794317','__spin_b':'trunk','__spin_t':'1673041526','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupCometJoinForumMutation','variables':'{"feedType":"DISCUSSION","groupID":"'+id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1673041528761,114928,2361831622,","group_id":"'+id+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":2,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}','server_timestamps':'true','doc_id':'5853134681430324','fb_api_analytics_tags':'["qpl_active_flow_ids=431626709"]',}
			try:
				join = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data).text
				if self.user_id in join:
					return True
				else:
					return join
			except:
				return False 

	def reac_cmt(self, id, type_react):
		access = ""
		url = requests.get("https://mbasic.facebook.com/"+id, headers=self.headers, proxies="").url
		if id in url:
			return False
		index = 1 if type_react == "LIKE" else 2 if type_react == "LOVE" else 3 if type_react == "CARE" else 4 if type_react == "HAHA" else 5 if type_react == "WOW" else 6 if type_react == "SAD" else 7
		access = requests.get(url, headers=self.headers).text
		while True:
			if id in access:
				find_cmt = access.split(id)[1].split('</a></span></span>')[0].split('/reactions/picker/?')[1].split('"')[0].replace("amp;", "")
				access = requests.get("https://mbasic.facebook.com/reactions/picker/?"+find_cmt, headers=self.headers).text
				ufi = access.split('/ufi/reaction/?')
				hoan_thanh = requests.get("https://mbasic.facebook.com/ufi/reaction/?"+ufi[index].split('"')[0].replace("amp;", ""), headers=self.headers).text
				return True
			else:
				if "/comment/replies/" in url:
					xemthemcmt = access.split('/comment/replies/?')[1].split('"')[0].replace("amp;", "")
					access = requests.get("https://mbasic.facebook.com/comment/replies/?"+xemthemcmt, headers=self.headers).text
				else:
					xemthemcmt = access.split('/story.php?')[1].split('</a></div></div>')[0].replace("amp;", "").split('"')[0]
					access = requests.get("https://mbasic.facebook.com/story.php?"+xemthemcmt, headers=self.headers).text
	def like(self, id, type):
		if '_' in id:
			uid = id.split('_')[1]
		else:
			uid = id
		list = {'LIKE':1, 'LOVE':2, 'CARE':3, 'HAHA':4, 'WOW':5, 'SAD':6, 'ANGRY':7}
		headers = {
        "authority": "mbasic.facebook.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua-mobile": "?0",
        'sec-ch-ua-platform': '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
        "cookie":self.cookie
}
		
		try:
			link = 'https://mbasic.facebook.com/reactions/picker/?ft_id='+uid
			data = requests.get(link, headers=self.headers).text
			get = data.split('<a href="')
			cx = get[list[type]].split('" style="display:block">')[0].replace("amp;", "").replace(";", "&")
			reac = requests.get('https://mbasic.facebook.com'+cx, headers = self.headers).text
			return True
		except:
			return False 
	
	def comment (self, id, msg):
		try:
			#headers = {"authority": "mbasic.facebook.com","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?0",'sec-ch-ua-platform': '"Windows"',"sec-fetch-dest": "document","sec-fetch-mode": "navigate","sec-fetch-site": "none","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",'user-agent: "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","cookie":self.cookie}
			url = requests.get("https://mbasic.facebook.com/"+id, headers=self.headers).url
			access = requests.get(url, headers=self.headers).text
			cmt = re.findall('\/a\/comment.php\?fs=.*?"', access)
			if cmt == []: return False
			hoan_thanh = requests.post("https://mbasic.facebook.com%s"%cmt[0].replace('"', "").replace("amp;", ""), headers=self.headers, data={"fb_dtsg": self.fb_dtsg,"jazoest": self.jazoest, "comment_text": msg}).text
			return hoan_thanh
		except:
			return False
	
	def share(self, id, nd):
		try:
			url = requests.get('https://mbasic.facebook.com/'+id, headers=self.headers).url
			ac = requests.get(url, headers=self.headers).text
			node_share = re.findall('\/composer\/mbasic\/\?c_src=share.*?"', ac)
			if node_share == []:
				return False
			truycapshare = ac.split('/composer/mbasic/?c_src=share')[1].split('"')[0].replace('amp;', '')
			ac = requests.get('https://mbasic.facebook.com/composer/mbasic/?c_src=share'+truycapshare, headers=self.headers).text
			fb = ac.split('name="fb_dtsg" value="')[1].split('"')[0]
			jaz = ac.split('name="jazoest" value="')[1].split('"')[0]
			target = ac.split('name="target" value="')[1].split('"')[0]
			csid = ac.split('name="csid" value="')[1].split('"')[0]
			privacyx = ac.split('name="privacyx" value="')[1].split('"')[0]
			sid = ac.split('name="sid" value="')[1].split('"')[0]

			data = {
           "fb_dtsg": fb,
            "jazoest": jaz,
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
            "xc_message": nd,
            "view_post": "Chia sáº»",
            "shared_from_post_id": sid,
        }
			share = ac.split('/composer/mbasic/?csid=')[2].split('"')[0].replace('amp;', '')
			hoan_thanh = requests.post('https://mbasic.facebook.com/composer/mbasic/?csid='+share, headers=self.headers, data=data).text
			return True
		except:
			return False 
class TraoDoiSub_Api (object):
	def __init__ (self, token):
		self.token = token
	
	def main(self):
		try:
			main = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+self.token).json()
			try:
				return main['data']
			except:
				False
		except:
			return False 
	
	def run(self, id):
		try:
			run = requests.get(f'https://traodoisub.com/api/?fields=run&id={id}&access_token={self.token}').json()
			try:
				run['data']['id']
				return True
			except:
				return False
		except:
			return False
	def get_job(self, type):
		try:
			get = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={self.token}',headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})
			return get
		except:
			return False 
		
	def nhan_xu(self, type, id):
		try:
			nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}',headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}).json()
			try:
				xu = nhan['data']['xu']
				msg = nhan['data']['msg']
				return msg, xu
			except:
				return nhan
		except:
			return False