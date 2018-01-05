import requests
import json
from pprint import pprint 
import urllib3
 



api_url_base = 'https://api.wigle.net/api/v2/profile/user'

headers = {'Content-Type': 'application/json',
		   'Authorization': 'Basic QUlEZmRkMmFiNTA1MDY1NDYxNDI5MjliZmNjMzk3N2I4NDE6YTIzZWMyNTA2M2Q5NTc4MWI1MjFhYWViMDI4YmNkY2I='}

r = requests.get(api_url_base, headers=headers)

d = r.json() 

print('HTTP Status Code =', r.status_code)

print('username: ',d['userid'])
print('email: ',d['email'])

api_url_base = 'https://api.wigle.net/api/v2/profile/apiToken'

headers = {'Content-Type': 'application/json',
		   'Authorization': 'Basic QUlEZmRkMmFiNTA1MDY1NDYxNDI5MjliZmNjMzk3N2I4NDE6YTIzZWMyNTA2M2Q5NTc4MWI1MjFhYWViMDI4YmNkY2I='}

r = requests.get(api_url_base, headers=headers)

d = r.json() 
print('authName: ',d['result'][0]['authName'])
print('token: ',d['result'][0]['token'])



api_url_base = 'https://api.wigle.net/api/v2/stats/user'

headers = {'Content-Type': 'application/json',
		   'Authorization': 'Basic QUlEZmRkMmFiNTA1MDY1NDYxNDI5MjliZmNjMzk3N2I4NDE6YTIzZWMyNTA2M2Q5NTc4MWI1MjFhYWViMDI4YmNkY2I='}

r = requests.get(api_url_base, headers=headers)

d = r.json() 
print('overall rank: ',d['statistics']['rank'])
print('monthRank: ',d['statistics']['monthRank'])
print('discoveredWiFi: ',d['statistics']['discoveredWiFi'])
print('discoveredCell: ',d['statistics']['discoveredCell'])






