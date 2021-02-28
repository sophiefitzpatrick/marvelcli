import click
import datetime

from marvelcli import utils
from marvelcli.workspace import workspace_queries

@click.option('-e', '--email', type=str, multiple=True, help='Use this flag for each email address you want removed from your workspace')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def remove_users_from_workspace(email: list, auth: str):
	"""Remove users from your workspace"""
	params = {'emails': email}
	query = workspace_queries.remove_users_from_workspace_query
	r, json_data = utils.make_request(auth, query, params)

	if not email:
		click.echo('Looks like you are missing some args, add `--help` to the command to see the options')
	if r.status_code != 200:
		if not email:
			click.echo('Looks like you are missing some args, add `--help` to the command to see the options')
		else:
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
		if plan['title'] != 'Free':
			click.echo("Price: %s %s" % (price, billing['currency'].upper()))
			click.echo("Seats: %s (%s %s per user)" % (plan['teamMembers'], price_per_seat, billing['currency'].upper()))
			click.echo("Projects: Unlimited \n")
		else:
			click.echo("Seats: %s " % (plan['teamMembers']))
			click.echo("Projects: 1 \n")

		click.echo(utils.colour.BOLD + "Your Usage" + utils.colour.END)
		click.echo("Seats Purchased: %s" % billing['seatQuantityPurchased'])
		click.echo("Seats Used: %s" % billing['seatQuantityUsed'])
		click.echo("Projects: %s \n" % billing['projectQuantityUsed'])

		if plan['title'] != 'Free':
			next_payment_date = billing['nextPaymentDate']
			dt = datetime.datetime(int(next_payment_date[0:4]), int(next_payment_date[5:7]), int(next_payment_date[8:10]), 0, 0)
			next_payment_date = "%s-%s-%s" % (dt.day, dt.month, dt.year)
			next_payment_amount = price_per_seat * billing['seatQuantityPurchased']
			click.echo("Your next payment date is %s. You'll be paying %s %s for %s seats.\n" % (next_payment_date, next_payment_amount, billing['currency'].upper(), billing['seatQuantityPurchased']))
		else:
			click.echo("Upgrade to create more projects and add more team members: https://marvelapp.com/plans\n")
