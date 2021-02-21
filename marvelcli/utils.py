import requests
import json
import os

def api_request(access_token, query, params=None):
	base_url = 'https://marvelapp.com/graphql'
	return requests.post(
		base_url,
		headers={'Authorization': 'Bearer {}'.format(access_token)},
		json={'query': query, 'variables': params}
	)

def get_access_token(auth=None):
	if auth:
		access_token = auth
		os.environ['MARVEL_CLI_TOKEN'] = access_token
	elif os.environ.get('MARVEL_CLI_TOKEN'):
		access_token = os.environ.get('MARVEL_CLI_TOKEN')
	else:
		access_token = input("Your auth code: ")
		os.environ['MARVEL_CLI_TOKEN'] = access_token

	return access_token

def make_request(auth, query, params=None):
	access_token = get_access_token(auth)
	if not params:
		r = api_request(access_token, query)
	else:
		r = api_request(access_token, query, params)
	json_data = json.loads(r.text)

	return r, json_data

class colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
