#! /usr/bin python
# -*- coding: utf-8 -*-




from threading import Thread

import os
from strgen import StringGenerator
import requests
import urllib.request
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

colorama.init()




print(Fore.BLUE + '''
╦ ╔═╗               
║ ╚═╗               
╩═╝╚═╝               
╔═╗┬─┐┌─┐┌┐ ┌┐ ┌─┐┬─┐
║ ╦├┬┘├─┤├┴┐├┴┐├┤ ├┬┘
╚═╝┴└─┴ ┴└─┘└─┘└─┘┴└
''')
print("...............coded by https://github.com/restanse")

print(Style.RESET_ALL)
count = input("enter count of threads: ")
count = int(count)

domlink = "https://prnt.sc/"
user_agents = { 'User-agent' : 'Mozilla / 5.0 (X11; Linux x86_64; rv: 70.0) Gecko / 20100101 Firefox / 70.0' }
check = os.path.exists("saved")


opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

if check == False:
	os.mkdir("saved")

os.chdir("saved")


def parsing():
	
	while True:

		val = StringGenerator("[\d\w]{6}").render().lower()
	
		url = domlink + val
	

		r = requests.get(url,headers = user_agents)

		if r.status_code == 200:
			html = r.text
			soup = BeautifulSoup(html, 'lxml')
                           

		
			try:
				t = soup.find("img", crossorigin="anonymous", alt="Lightshot screenshot", id="screenshot-image")

		#	
				link = t["src"]
			except:
				continue
			name = link.split('/')[-1]
		
		
		
			if link.split("/")[0] == "https:":
			
			
				

				urllib.request.urlretrieve(link, name)
				

				print(Fore.BLUE + "found: " + url + ". "+name+" saved to "+ os.getcwd())
			
		
#img class="no-click screenshot-image"



for thrs in range(1, count):
	thr = Thread(target = parsing)
	thr.start()
