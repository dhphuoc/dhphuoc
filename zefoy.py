import re, requests, base64, os
from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
from time import sleep
from io import BytesIO
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
os.system("cls" if os.name == "nt" else "clear")
def parse_time(text):
    minutes = re.search(r'(\d+) minute\(s\)', text)
    seconds = re.search(r'(\d+) seconds', text)
    minutes = int(minutes.group(1)) if minutes else 0
    seconds = int(seconds.group(1)) if seconds else 0
    total_seconds = minutes * 60 + seconds
    sleep(total_seconds)    

def get_captcha():
    js_script = '''
        var img = document.querySelector("body > div.noscriptcheck > div.ua-check > form > div > div > img");
        var canvas = document.createElement('canvas');
        canvas.width = img.width;
        canvas.height = img.height;
        var ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0, img.width, img.height);
        return canvas.toDataURL('image/png').substring(22);  // Loại bỏ phần đầu "data:image/png;base64,"
    '''
    image_base64 = driver.execute_script(js_script)
    image_data = base64.b64decode(image_base64)
    image_name = 'captcha.png'
    image = Image.open(BytesIO(image_data))
    image.save(image_name)

def slove():
    while True:
        try:
            task = 'captcha.png'
            request = requests.post('https://api.ocr.space/parse/image?K87899142388957', headers={'apikey':'K86619931688957'}, files={'task':open(task,'rb')}).json()
            solved_text = request['ParsedResults'][0]['ParsedText']
            print(f'CAPTCHA: {solved_text.strip()}')
            return solved_text.strip()
        except:
            pass

chrome_options = Options()
chrome_options.add_argument("--window-size=600,900")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--display=:1")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://zefoy.com/")
os.system("cls" if os.name == "nt" else "clear")
def loggin():
    while True:
        html = driver.page_source
        while True:
            if 'Enter the word' in html:
                break
            else:
                sleep(2)
                
                tieu_de = driver.title
                if tieu_de != 'Zefoy':
                    pass
        sleep(0.3)
        get_captcha()
        captcha_text = slove()
        if captcha_text == '':
            captcha_text = 'dhphuoc'
        sleep(1)
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.noscriptcheck > div.ua-check > form > div > div > div > input")))
        js_script = '''
        document.querySelector("body > div.noscriptcheck > div.ua-check > form > div > div > div > input").value = arguments[0];
        '''
        driver.execute_script(js_script, captcha_text)
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.noscriptcheck > div.ua-check > form > div > div > div > div > button")))
        js_script = '''
        document.querySelector("body > div.noscriptcheck > div.ua-check > form > div > div > div > div > button").click();
        '''
        driver.execute_script(js_script)
        while True:
            sleep(0.5)
            html = driver.page_source
            if 'Captcha code is incorrect.' in html:  
                print('GIẢI CAPTCHA SAI !!! ')
                driver.refresh()
                hvthu = 'off'
                break
            elif 'button class="btn btn-primary rounded-0 t-views-button"><i class="fa fa-arrow-right fa-lg"></i></button>' in html:
                print('GIẢI CAPTCHA THÀNH CÔNG ')
                hvthu = 'on'
                break
            else:
                pass
        if hvthu == 'on':
            break
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', class_='col-sm-4 col-xs-12 p-1 colsmenu')
    titles = []
    for div in divs:
        h5_tag = div.find('h5', class_='card-title')
        print(h5_tag.text.strip())
        try:
            small_tag = div.find('small', class_='badge badge-round badge-danger d-sm-inline-block')
            print(small_tag.text)
        except:
            small_tag = div.find('small', class_='badge badge-round badge-warning d-sm-inline-block')
            print(small_tag.text)
    sleep(1)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(9) > div > div.noscriptcheck > div > div > div:nth-child(6) > div > button")))
        js_script = '''
        document.querySelector("body > div:nth-child(9) > div > div.noscriptcheck > div > div > div:nth-child(6) > div > button").click();
        '''
        driver.execute_script(js_script)
    except:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(8) > div > div.noscriptcheck > div > div > div:nth-child(6) > div > button")))
            js_script = '''
            document.querySelector("body > div:nth-child(8) > div > div.noscriptcheck > div > div > div:nth-child(6) > div > button").click();
            '''
            driver.execute_script(js_script)
        except:
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(11) > div > div.noscriptcheck > div > div > div:nth-child(6) > div > button")))
                js_script = '''
                document.querySelector("body > div:nth-child(11) > div > div.noscriptcheck > div > div > div:nth-child(6) > div > button").click();
                '''
                driver.execute_script(js_script)
            except:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(10) > div > div.noscriptcheck > div > div > div:nth-child(6) > div > button")))
                js_script = '''
                document.querySelector("body > div:nth-child(10) > div > div.noscriptcheck > div > div > div:nth-child(6) > div > button").click();
                '''
                driver.execute_script(js_script)
    print('ĐÃ MỞ VIEW !!! ')
loggin()
sleep(1)
video = input('Nhập Link Video: ')
while True:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.col-sm-5.col-xs-12.p-1.container.t-views-menu > div > form > div > input")))
    js_script = '''
    document.querySelector("body > div.col-sm-5.col-xs-12.p-1.container.t-views-menu > div > form > div > input").value = arguments[0];
    '''
    driver.execute_script(js_script, video)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.col-sm-5.col-xs-12.p-1.container.t-views-menu > div > form > div > div > button")))
    js_script = '''
    document.querySelector("body > div.col-sm-5.col-xs-12.p-1.container.t-views-menu > div > form > div > div > button").click();
    '''
    driver.execute_script(js_script)
    try:
        while True:
            try:
                while True:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > span.br.views-countdown')))
                    html = driver.execute_script('return document.querySelector("#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > span.br.views-countdown").outerHTML')
                    pattern = r'<span class="br views-countdown" style="text-align:center;color:#337ab7;font-weight:bold;font-size:115%;">(.*?)</span>'
                    match = re.search(pattern, html)
                    if match:
                        extracted_text = match.group(1)
                    text = extracted_text
                    if text.strip() != 'Checking Timer...' and text.strip() != 'Next Submit: READY....!':
                        break
                print(text)
                parse_time(text)
                sleep(1)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.col-sm-5.col-xs-12.p-1.container.t-views-menu > div > form > div > div > button")))
                js_script = '''
                document.querySelector("body > div.col-sm-5.col-xs-12.p-1.container.t-views-menu > div > form > div > div > button").click();
                '''
                driver.execute_script(js_script)
                sleep(3)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > div.row.text-light.d-flex.justify-content-center > div > form > button')))
                js_script = '''
                document.querySelector("#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > div.row.text-light.d-flex.justify-content-center > div > form > button").click();
                '''
                driver.execute_script(js_script)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > span:nth-child(3)')))
                    html = driver.execute_script('return document.querySelector("#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > span:nth-child(3)").outerHTML')
                    pattern = r'<span style="font-size:110%;font-weight:bold;font-family:Arial, Helvetica, sans-serif;text-align:center;color:green;">(.*?)</span>'
                    match = re.search(pattern, html)
                    if match:
                        view = match.group(1)
                    print(view)
                except:
                    pass
                sleep(5)
                
            except:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > div.row.text-light.d-flex.justify-content-center > div > form > button')))
                js_script = '''
                document.querySelector("#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > div.row.text-light.d-flex.justify-content-center > div > form > button").click();
                '''
                driver.execute_script(js_script)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > span:nth-child(3)')))
                    html = driver.execute_script('return document.querySelector("#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > span:nth-child(3)").outerHTML')
                    pattern = r'<span style="font-size:110%;font-weight:bold;font-family:Arial, Helvetica, sans-serif;text-align:center;color:green;">(.*?)</span>'
                    match = re.search(pattern, html)
                    if match:
                        view = match.group(1)
                    print(view)
                except:
                    pass
                sleep(5)
    except:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > div')))
            driver.refresh()
            loggin()
        except:
            pass
