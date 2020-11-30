import sys
import click
import requests
import json

@click.group()
def main(args=None):
    """A CLI wrapper for Marvelapp

	The wrapper will enable you to interact with your Marvel
	account from the comfort of your command line.

	To auth each command you'll need to use the -a flag with
	your access token key.

	You can generate a new one here or find the one you
	already have set up: https://marvelapp.com/oauth/devtoken

	"""

BASE_URL = 'https://marvelapp.com/graphql'

@click.option('-p', '--pk', help='Pk of the project you want to delete')
@click.option('-a', '--auth', help='Auth your request')
@main.command()
def delete_project(pk: str, auth: str):
	"""Delete a project"""
	params = {
        'pk': pk,
    }

	if auth:
		access_token = auth
	else:
		access_token = input("Your auth code: ")

	query = '''
		mutation deleteproject ($pk: Int!) {
			deleteProject(input: {pk: $pk}) {
                ok
            }
        }
    '''

	r = requests.post(
		BASE_URL,
		headers={'Authorization': 'Bearer {}'.format(access_token)},
		json={'query': query, 'variables': params}
	)

	json_data = json.loads(r.text)

	if r.status_code != 200:
		print('\n' + 'Project could not be deleted from your account' + '\n')
		print(json_data)
	else:
		print('"%s" has been successfully deleted from your Marvel account' % pk)

@click.option('-n', '--name', help='Name of project')
@click.option('-p', '--password', help='Project password')
@click.option('-a', '--auth', help='Auth your request')
@main.command()
def create_project(name: str, password: str, auth: str):
	"""Create a new project"""
	params = {
        'name': name,
        'password': password
    }

	if not password:
		params['password'] = ''

	if auth:
		access_token = auth
	else:
		access_token = input("Your auth code: ")

	query = '''
		mutation createproject ($name: String!, $password: String!) {
			createProject(input: {name: $name, password: $password}) {
                ok
            }
        }
    '''

	r = requests.post(
		BASE_URL,
		headers={'Authorization': 'Bearer {}'.format(access_token)},
		json={'query': query, 'variables': params}
	)

	json_data = json.loads(r.text)

	if r.status_code != 200:
		print('\n' + 'A new project could not be created at this time, see the error below"' + '\n')
		print(json_data)
	else:
		print('"%s" has been successfully created in your Marvel account' % name)

@click.option('-a', '--auth', help='Auth your request')
@main.command()
def personal_projects(auth: str):
	"""List all projects owned by you"""
	if auth:
		access_token = auth
	else:
		access_token = input("Your auth code: ")

	query = '''
		query {
			user {
				projects {
					edges {
						node {
							prototypeUrl
						}
					}
				}
			}
		}
	'''

	r = requests.post(BASE_URL, headers={'Authorization': 'Bearer {}'.format(access_token)}, json={'query': query})
	json_data = json.loads(r.text)

	data = json_data['data']['user']['projects']['edges']

	urls = []
	for d in data:
		url = d['node']['prototypeUrl']
		urls.append(url)

	project_count = len(json_data['data']['user']['projects']['edges'])
	print('You have {} project(s)'.format(project_count))

	for url in urls:
		print(url)

if __name__ == "__main__":
    sys.exit(main())
