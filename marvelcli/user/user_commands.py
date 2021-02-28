import click
import datetime

from marvelcli import utils
from marvelcli.user import user_queries

@click.option('-a', '--auth', help='Auth your request')
@click.command()
def about_user(auth: str):
	"""User statistics"""
	query = user_queries.about_user_query
	r, json_data = utils.make_request(auth, query)

	if r.status_code != 200:
		click.echo("\nWe could not retrieve the data at this time, possibly due to a ratelimit. Try again in a few minutes\n")
	else:
		user = json_data['data']['user']
		last_active = user['lastActiveAt']
		last_active = datetime.datetime(int(last_active[0:4]), int(last_active[5:7]), int(last_active[8:10]), 0, 0)

		click.echo(utils.colour.BOLD + '\nYour Account:' + utils.colour.END)
		click.echo('Email: %s' % user['email'])
		click.echo('Last Active: %s' % last_active)
		click.echo('Status: %s' % user['status'])
		click.echo('Username: %s \n' % user['username'])
