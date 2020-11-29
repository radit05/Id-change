import requests
from time import sleep
from getpass import getpass
from datetime import datetime
import json
import sys
import os
import random
import websocket
import time, datetime
from datetime import datetime
import time, requests, random
API_BASE_URL = "https://id-api.spooncast.net"
API_LOGIN = '/signin/'
API_USER = '/users/'
API_IDCHANGE = 'username/'
paramex = {'cv':'heimdallr'}
os.system ('clear')
print ("FITUR GANTI ID")
print ("BY RADIT")

nomerhp = input("Masukan Nomor HP : ")
passwordhp = input("Masukan Password : ")
sleep(1)
print('Sedang Login >>>')
headers1={'User-Agent':'Spoon/4.3.22(203) Dalvik/2.1.0 (Linux; U; Android 9; Redmi 4X Build/PQ2A.190305.002'}
auth = {'sns_type':'phone','sns_id':nomerhp,'password':passwordhp}
r = requests.post(API_BASE_URL + API_LOGIN ,headers=headers1, json=auth)
respon_data = r.json()
for i in respon_data['results']:
		taguser = i['id']
		tokennyaa = i['token']
		idbaru = input('Masukan ID yang baru : ')
		inputidbaru = {'username':idbaru}
		headers = {'Authorization':'Token ' + tokennyaa,
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		"origin":"https://www.spooncast.net",
		"referer":"https://www.spooncast.net/",
		'content-type':'application/json',
		'User-Agent':'AppleWebKit/537.36 Mozilla'}
		rid = requests.post(API_BASE_URL + API_USER + API_IDCHANGE,headers=headers,params=paramex,json=inputidbaru)
		if rid.status_code == 200:
			print('Success ! ID Telah di ganti ke ' + str(idbaru))
			print('Silahkan Cek ID Spoon kamu..')