import requests
import json

url = 'http://127.0.0.1:8000/login/'

data = {
	'username':'test',
	'password':'123456'

}

# def send_post(url,data):
res = requests.post(url=url,data=data)
	# return res.json()

print(res.json())

