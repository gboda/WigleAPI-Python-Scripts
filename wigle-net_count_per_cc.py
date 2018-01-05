import requests
import json
from pprint import pprint 
import urllib3
 

while True: 
	
	cc = input('Address: ')

	api_url_base = 'https://api.wigle.net/api/v2/stats/countries'

	headers = {'Content-Type': 'application/json',
			   'Authorization': 'Basic QUlEZmRkMmFiNTA1MDY1NDYxNDI5MjliZmNjMzk3N2I4NDE6YTIzZWMyNTA2M2Q5NTc4MWI1MjFhYWViMDI4YmNkY2I='}

	r = requests.get(api_url_base, headers=headers)

	d = r.json() 

	print('HTTP Status Code =', r.status_code)

	a = next((item for item in d['countries'] if item["country"] == cc))
	print(a)


#generator expression https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search