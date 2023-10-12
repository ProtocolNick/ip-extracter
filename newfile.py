# domain2ip.py

import os
import sys
import socket
import colorama
from colorama import Fore,Back,Style

#  if u want add threading urself , in my case i do not need it so...
if sys.platform.startswith('linux'):
	os.system('clear')
else:
	os.system('cls')
colorama.init(autoreset=True)
banner = """\t[+]welcome[+]
\t[+] domain to ip script [+]


""".title()
print(banner)
def domain2ip():
	file_path = input("Enter site list : ")
	with open(file_path,'r') as file:
		urls = file.readlines()
		urls = [url.strip() for url in urls]
		print("Total uRLs :",len(urls))
		for domain in urls:
			if domain.startswith("http"):
				domain = domain.replace("https://", "").replace("http://", "")

			try:
				ip = socket.gethostbyname(domain)
				print(Fore.GREEN+Style.BRIGHT+ '[+]Domain:'+Fore.BLUE+Style.BRIGHT+f"{domain}"+'\n'+Fore.RED+Style.BRIGHT+ '[+]IP :'+Fore.GREEN+Style.BRIGHT + f'{ip}')
				save = open('ips.txt','a')
				save.write(ip+'\n')
			except socket.gaierror:
				print(f'Faild to resolve ip for {domain}')
domain2ip()




		



		
