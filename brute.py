import threading
import random
import string
import requests
import codecs
print("started")
inviteLength = 7
threadCount = 25
cache = {}
def gen_invite(length=7, chars=(string.ascii_uppercase+string.ascii_lowercase+string.digits)):
	return ''.join(random.choices(chars, k=length))
def get_invite(invite):
	req = requests.get("https://discordapp.com/api/v6/invites/"+invite)
	return req.json()
def check_invite(invite):
	req = requests.delete("https://discordapp.com/api/v6/invites/"+invite, headers={"Authorization": codecs.decode("AQD2ZGH0ZwL0AmN4BGN3ZQV4.Qq05Tj.ktoiyIAm226k7ZkEZBFo9wcheMH", "rot-13")})
	if req.status_code == 403:
		return True
def thread():
	while True:
		try:
			invite = gen_invite(length=inviteLength)
			if invite in cache:
				continue
			cache[invite] = 1
			if check_invite(invite):
				info = get_invite(invite)
				print(info["guild"]["name"], "discord.gg/"+invite)
				post("discord.gg/"+invite)
		except Exception as e:
			print("Error:", e)
for i in range(25):
	threading.Thread(target=thread).start()
def post(stuff):
    url = "https://discordapp.com/api/webhooks/479538399536218112/QringagIg9UTcc-Jd1BRBVThDKDmnosgLdJVQ9xHzeTecdk7A7d1TFJelamBMyOZJ4pH"
    payload = "content=" + stuff
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
