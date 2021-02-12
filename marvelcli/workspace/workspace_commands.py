import click
import datetime

import utils
from workspace import workspace_queries

@click.option('-e', '--email', type=str, multiple=True, help='Use this flag for each email address you want invited to your workspace')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def invite_users_to_workspace(email: list, auth: str):
	"""Invite users to your workspace"""
	params = {'emails': email, 'role': 'EDITOR'}
	query = workspace_queries.invite_users_to_workspace_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		click.echo('\n' + json_data['data']['inviteUsersToWorkspace']['error']['message'] + '\n')
	else:
		data_success = json_data['data']['inviteUsersToWorkspace']['succeeded']
		data_failed = json_data['data']['inviteUsersToWorkspace']['failed']

		if data_success:
			succeeded = "\nThe following people were successfully invited to your workspace: %s." % ', '.join(data_success)
			click.echo(succeeded + "They've been assigned the role of 'EDITOR'. \n")

		if data_failed:
			click.echo('\nThe following people could not be invited to your workspace:')
			for f in data_failed:
				click.echo("%s  - '%s'\n" % (f.get('email'), f.get('message')))

@click.option('-e', '--email', type=str, multiple=True, help='Use this flag for each email address you want removed from your workspace')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def remove_users_from_workspace(email: list, auth: str):
	"""Remove users from your workspace"""
	params = {'emails': email}
	query = workspace_queries.remove_users_from_workspace_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		click.echo('\n' + json_data['data']['removeUsersFromWorkspace']['error']['message'] + '\n')
	else:
		data_success = json_data['data']['removeUsersFromWorkspace']['succeeded']
		data_failed = json_data['data']['removeUsersFromWorkspace']['failed']

		if data_success:
			succeeded = "\nThe following people were successfully removed from your workspace: %s \n" % ', '.join(data_success)
			click.echo(succeeded)

		if data_failed:
			click.echo('\nThe following people could not be removed from your workspace:')
			for f in data_failed:
				click.echo("%s  - '%s'\n" % (f.get('email'), f.get('message')))


@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def get_billing_info(auth: str):
	"""Get billing information"""
	query = workspace_queries.get_billing_info_query
	r, json_data = utils.make_request(auth, query)

	if r.status_code != 200:
		click.echo('\n' + 'Billing data could not be returned right now.' + '\n')
	else:
		billing = json_data['data']['user']['company']['billing']
		plan = billing['plan']

		if billing['billingCycle'] == 'yearly':
			price = int(plan['priceYearly'] / 100)
			price_per_seat = round(price / billing['seatQuantityUsed'], 2)
		else:
			price = int(plan['priceMonthly'] / 100)
			price_per_seat = round(price / billing['seatQuantityUsed'], 2)

		click.echo(utils.colour.BOLD + "\nYour Plan" + utils.colour.END)
		click.echo("Type: %s" % plan['title'])
		click.echo("Price: %s %s" % (price, billing['currency'].upper()))
		click.echo("Seats: %s (%s %s per user)" % (plan['teamMembers'], price_per_seat, billing['currency'].upper()))
		if plan['title'] != 'Free':
			click.echo("Projects: Unlimited \n")
		else:
			click.echo("Projects: 1 \n")

		click.echo(utils.colour.BOLD + "Your Usage" + utils.colour.END)
		click.echo("Seats Purchased: %s" % billing['seatQuantityPurchased'])
		click.echo("Seats Used: %s" % billing['seatQuantityUsed'])
		click.echo("Projects: %s \n" % billing['projectQuantityUsed'])

		next_payment_date = billing['nextPaymentDate']
		dt = datetime.datetime(int(next_payment_date[0:4]), int(next_payment_date[5:7]), int(next_payment_date[8:10]), 0, 0)
		next_payment_date = "%s-%s-%s" % (dt.day, dt.month, dt.year)
		next_payment_amount = price_per_seat * billing['seatQuantityPurchased']
		click.echo("Your next payment date is %s for %s %s for %s seats\n" % (next_payment_date, next_payment_amount, billing['currency'].upper(), billing['seatQuantityPurchased']))
