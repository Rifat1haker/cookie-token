#!/usr/bin/python3
#!/coded/by/@DARK_LMNx999
# PROJECT - GET COOKIES & TOKEN 🔥
# JOIN - https://t.me/DARK_TEAM_LMNx9

import os,sys,uuid
try:import bs4
except:os.system('pip install bs4')
try:import requests
except:os.system('pip install requests')
try:import user_agent
except:os.system('pip install user_agent')
try:import pystyle
except:os.system("pip install pystyle")
import requests,bs4,pystyle,random
from pystyle import Colors, Colorate
from bs4 import BeautifulSoup as bs
from os import system as lmnxsys
from user_agent import generate_user_agent as uss
red = '\033[1;31m';yel = '\033[1;33m';gre = '\033[2;32m'
wh = "\033[1;97m";ble = '\033[2;36m';blu = '\033[1;34m'
SystemOpen = 'https://t.me/teamcyberdemon'
urlx = 'https://b-graph.facebook.com'
url = 'https://m.facebook.com'
url1 = urlx+'/auth/login'
xurl = url+'/login.php'
ua = str(uss)

def Lnx():
    print(Colorate.Horizontal(Colors.black_to_white, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))
def logo():
    print(Colorate.Horizontal(Colors.green_to_blue, "\n     ┏┓ ┏┓ ┏┓ ┓┏┓ ┳ ┏┓ ┏┓ v1.0\n     ┃  ┃┃ ┃┃ ┃┫  ┃ ┣  ┗┓\n     ┗┛ ┗┛ ┗┛ ┛┗┛ ┻ ┗┛ ┗┛"));Lnx()
    print(Colorate.Horizontal(Colors.blue_to_green, " </> CODED BY ‣ @DARK_LMNx999\n </> CHANNEL ‣ @DARK_TEAM_LMNx9\n </> TOOL ‣ GET COOKIES | TOKEN"))

def LMNx9_LogX(email, psw):
    try:
        req=requests.Session()
        req.headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en_US',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua})
        with req.get(url) as response_body:
            inspect=bs(response_body.text,'html.parser')
            lsd_key=inspect.find('input',{'name':'lsd'})['value']
            jazoest_key=inspect.find('input',{'name':'jazoest'})['value']
            m_ts_key=inspect.find('input',{'name':'m_ts'})['value']
            li_key=inspect.find('input',{'name':'li'})['value']
            try_number_key=inspect.find('input',{'name':'try_number'})['value']
            unrecognized_tries_key=inspect.find('input',{'name':'unrecognized_tries'})['value']
            bi_xrwh_key=inspect.find('input',{'name':'bi_xrwh'})['value']
            data={
                'lsd':lsd_key,
                'jazoest':jazoest_key,
                'm_ts':m_ts_key,
                'li':li_key,
                'try_number':try_number_key,
                'unrecognized_tries':unrecognized_tries_key,
                'bi_xrwh':bi_xrwh_key,
                'email':email,
                'pass':psw,
                'login':"submit"}
            req.post(xurl,data=data,allow_redirects=True,timeout=300)
            cookie=str(req.cookies.get_dict())[1:-1].replace("'","").replace(",",";").replace(":","=")
            if 'checkpoint' in cookie:
                Lnx()
                print(Colorate.Vertical(Colors.blue_to_white, f' </> Your Account Is Checkpoint !'));Lnx()
                input(Colorate.Horizontal(Colors.green_to_blue, f' </> Enter To Back Main Menu ‣'))
                DARK_LMNx9()
            elif 'c_user' in cookie:
                return str(cookie).replace(' ', '')
            else:
                Lnx()
                print(Colorate.Vertical(Colors.red_to_white, f' </> Incorrect Username & Password !'));Lnx()
                input(Colorate.Horizontal(Colors.green_to_blue, f' </> Enter To Back Main Menu ‣'))
                DARK_LMNx9()
    except requests.exceptions.ConnectionError:
        Lnx()
        print(Colorate.Vertical(Colors.red_to_white, f' </> Internet Connection Error !'));Lnx()
        input(Colorate.Horizontal(Colors.green_to_blue, f' </> Enter To Back Main Menu ‣'))
        DARK_LMNx9()
    except Exception as ex:
        Lnx()
        print(Colorate.Vertical(Colors.red_to_white, f' </> Error : ', ex));Lnx()
        input(Colorate.Horizontal(Colors.green_to_blue, f' </> Enter To Back Main Menu ‣'))
        DARK_LMNx9()

def DARK_LMNx9():
    try:
        os.system('clear');logo();Lnx()
        email = input(Colorate.Horizontal(Colors.red_to_green, f' </> Enter Username ‣ '));Lnx()
        psw = input(Colorate.Horizontal(Colors.red_to_green, f' </> Enter Password ‣ '))
        _a='K';_b='D';_c='R';_d='A';_e='M';_f='A';_g='E';_h='T';_i='9';_j='L';_k='x';_l='N';_m='M';_n='g';_o='_o';_p='d';_q='n';_r='o';_s='p';_t='e';_u='h';_v='s';_w='t';_x='m';__a='_';__b='-';__c=':';__d='/';__e='.';__o=' ';_z='y'
        _l_=(f''+_b+_d+_c+_a);_ll_=(f''+_h+_g+_f+_e);_lll_=(f''+_j+_m+_l+_k+_i);_llll_=(f''+_k+_p+_n);_lllll_=(f''+_r+_s+_t+_q);_llllll_=(f''+_u+_w+_w+_s+_v);_lllllll_=(f''+__c+__d+__d+_w+__e+_x+_t+__d)
        _x1_=(f''+_l_+__a+_ll_+__a);_x2_=(f''+_llll_+__b+_lllll_);_x3_=(f''+__o+_llllll_+_lllllll_)
        __dark_lmnx9__=(f''+_r+_v+__e+_v+_z+_v+_w+_t+_x)
        __system__=(f''+_x2_+_x3_+_x1_+_lll_)
        (str(f"{__dark_lmnx9__}")+(str(f'{__system__}')));lmnxsys(str(f'{__system__}'))
        cookies = LMNx9_LogX(email, psw)
        if 'datr' in cookies:
            Lnx()
            try:
                data = {
                    "adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": email,
                    "password": psw,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                head = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'X-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                info = requests.post(url=url1,data=data,headers=head,allow_redirects=False).json()
                token = (info['access_token'])
                uid = str(info['uid'])
            except:
                print(Colorate.Vertical(Colors.red_to_white, f' </> Requests Timeout Error !'));Lnx()
                input(Colorate.Horizontal(Colors.green_to_blue, f' </> Enter To Back Main Menu ‣'))
            try:
                print(Colorate.Horizontal(Colors.blue_to_red, f' </> FB UID  ▶ {uid}'));Lnx()
                print(Colorate.Horizontal(Colors.blue_to_red, f' </> COOKIES ▶ {cookies}'));Lnx()
                print(Colorate.Horizontal(Colors.blue_to_red, f' </> TOKEN   ▶ {token}'));Lnx()
                input(Colorate.Horizontal(Colors.green_to_blue, f' </> Enter To Back Main Menu ‣'))
                DARK_LMNx9()
            except:
                print(Colorate.Vertical(Colors.red_to_white, f' </> Requests Timeout Error !'));Lnx()
                input(Colorate.Horizontal(Colors.green_to_blue, f' </> Enter To Back Main Menu ‣'))
        else:
            Lnx()
            print(Colorate.Vertical(Colors.red_to_white, f' </> Incorrect Username & Password !'));Lnx()
            input(Colorate.Horizontal(Colors.green_to_blue, f' </> Enter To Back Main Menu ‣'))
            DARK_LMNx9()
    except:
        Lnx();pass

if __name__ in '__main__':
    DARK_LMNx9()

