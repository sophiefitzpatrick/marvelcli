import click
import datetime

from marvelcli import utils
from marvelcli.user import user_queries

@click.option('-o', '--old-password', type=str, help='Your old account password')
@click.option('-n', '--new-password', type=str, help='Your new account password')
@click.option('-a', '--auth', help='Auth your request')
@click.command()
def update_account_password(new_password: str, old_password: str, auth: str):
	"""Update your account password"""
	params = {'newPassword': new_password,'oldPassword': old_password}
	query = user_queries.password_update_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		click.echo('\n' + json_data['data']['updateUserPassword']['error']['message'] + '\n')
	else:
		click.echo("\nYour account updated with the new password successfully!\n")

@click.option('-p', '--password', type=str, help='Your account password to auth the change')
@click.option('-e', '--email', type=str, help='Your new email address')
@click.option('-o', '--occupation', type=str, help='Your occupation')
@click.option('-u', '--username', type=str, help='Your new username')
@click.option('-a', '--auth', help='Auth your request')
@click.command()
def update_user(password: str, occupation: str, email: str, username: str, auth: str):
	"""Update your email, username and occuption"""
	params = {'email': email,'username': username,'occupation': occupation,'password': password}
	query = user_queries.user_update_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code == 200:
		if not json_data['data']['updateCurrentUser']['ok']:
			click.echo('\n' + json_data['data']['updateCurrentUser']['error']['message'] + '\n')
		else:
			click.echo("\nYour account updated successfully!\n")
	else:
		click.echo("\nTry 'marvelcli update_user --help' to make sure you are not missing any args.\n")

@click.option('-a', '--auth', help='Auth your request')
@click.command()
def about_user(auth: str):
	"""User statistics"""
	query = user_queries.about_user_query
	r, json_data = utils.make_request(auth, query)

	user = json_data['data']['user']
	last_active = user['lastActiveAt']
	last_active = datetime.datetime(int(last_active[0:4]), int(last_active[5:7]), int(last_active[8:10]), 0, 0)

	if r.status_code != 200:
		click.echo("\nWe could not retrieve the data at this time, possibly due to a ratelimit. Try again in a few minutes\n")
	else:
		click.echo(utils.colour.BOLD + '\nYour Account: \n' + utils.colour.END)
		click.echo('Email: %s' % user['email'])
		click.echo('Last Active: %s' % last_active)
		click.echo('Has Password: %s' % user['hasPassword'] )
		click.echo('Status: %s' % user['status'])
		click.echo('Username: %s' % user['username'])
		click.echo(utils.colour.BOLD + '\nYour Statistics: \n' + utils.colour.END)
		click.echo('Number of Folders created by you: %s' % user['properties']['foldersOwnedCount'])
		click.echo('Number of Hotspots created by you: %s' % user['properties']['hotspotsOwnedCount'])
		click.echo('Number of Projects created by you: %s' % user['properties']['prototypeProjectsOwnedCount'])
		click.echo('Number of Groups created by you: %s' % user['properties']['teamsOwnedCount'])
		click.echo('Number of Screens created by you: %s' % user['properties']['screensOwnedCount'])
		click.echo('Number of Usertest Projects created by you: %s\n' % user['properties']['userTestProjectsOwnedCount'])
