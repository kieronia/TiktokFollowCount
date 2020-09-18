import argparse
import json
import os
import random
import requests
import sys
import time
from colorama import init, Fore, Back, Style
import datetime
init(convert=True)
from bs4 import BeautifulSoup
from useragents import *
from pygame import mixer 

username = "putausername"

#if your using this as just a cool follow count - remove the chunk of code related to mixer.music.load('sound.mp3') lines - it was put there this was made as a cool project to stop people faking that something happens when you follow them - do it the proper way XD
os.system(f"title // {username} \\\\")
time.sleep(1)
os.system('cls')



newfollowint = "0"
followint = "0"
newdif = "0"
while True:
	timetowait = random.randint(5,15)
	time.sleep(timetowait)
	r = requests.get(f'http://tiktok.com/@{username}', headers={'User-Agent':random.choice(user_agents)})
	soup = BeautifulSoup(r.text, "html.parser")
	content = soup.find_all("script", attrs={"type":"application/json", "crossorigin":"anonymous"})
	content = json.loads(content[0].contents[0])
	profile_data = {content["props"]["pageProps"]["userData"]["fans"]}
	followint = int(list(profile_data)[0])
	currentDT = datetime.datetime.now()
	hour = str(currentDT.hour)
	minute = str(currentDT.minute)
	second = str(currentDT.second)

	newdif = str(int(newfollowint) - int(followint))
	if newdif[0] == "-":
		print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Follower count for {Fore.WHITE}[{username}]{Fore.GREEN} = {Fore.WHITE}[{followint}]{Fore.GREEN} - Followers gained = {Fore.WHITE}[+{newdif[1:]}] ")#gained a follower
		face = "🙂"
		mixer.init()
		mixer.music.load('peepeepoopoo.mp3') #plays music - could make it play a sound effect upon losing a follower etc but no ones gonna follow you lmao
		mixer.music.play()
	elif newdif == "0":
		print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Follower count for {Fore.WHITE}[{username}]{Fore.GREEN} = {Fore.WHITE}[{followint}]{Fore.GREEN} - Followers gained = {Fore.WHITE}[0] ") #when it stays the same
		face = "😐"
	else:
		print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Follower count for {Fore.WHITE}[{username}]{Fore.GREEN} = {Fore.WHITE}[{followint}]{Fore.GREEN} - Followers lost = {Fore.WHITE}[-{newdif}] ") #lost a follower or error lol
		face = "🙁"
	os.system(f"title {face} // {username} // {str(followint)}")
	

#second time to work out dif over 5 seconds
	r = requests.get(f'http://tiktok.com/@{username}', headers={'User-Agent':random.choice(user_agents)}) #i coulda done this better but my projects literally get posted in discords where people remove every refrence to me and pretend they made it etc and make massive servers off projects they found online and don't even give a star - like its free - cmon. Once any post gets 10+ stars I'll make it look super fancy as I know yall are interested etc
	soup = BeautifulSoup(r.text, "html.parser")
	content = soup.find_all("script", attrs={"type":"application/json", "crossorigin":"anonymous"})
	content = json.loads(content[0].contents[0])
	profile_data = {content["props"]["pageProps"]["userData"]["fans"]}
	newfollowint = int(list(profile_data)[0])
