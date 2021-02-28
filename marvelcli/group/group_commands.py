import click

from marvelcli import utils
from marvelcli.group import group_queries

@click.option('-g', '--group-pk', type=int, multiple=True, help='Use this flag for each group to be deleted')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def delete_groups(group_pk: list, auth: str):
	"""Delete a list of groups"""
	params = {'groupPks': group_pk}
	query = group_queries.delete_groups_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		click.echo(json_data['data']['deleteGroups']['error']['message'])
	else:
		if not group_pk:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			data_success = json_data['data']['deleteGroups']['succeeded']
			data_failed = json_data['data']['deleteGroups']['failed']

			if data_success:
				click.echo("\nThe following groups were deleted from your workspace successfully: %s" % data_success)

			if data_failed:
				click.echo('\nThe following groups could not be deleted from your workspace:')
				for f in data_failed:
					click.echo("%s  - %s" % (f.get('groupPk'), f.get('message')))

			click.echo("\n")

@click.option('-n', '--name', type=str, help='Name of group')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def create_group(name: str, auth: str):
	"""Create a group"""
	params = {'name': name}
	query = group_queries.create_group_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code == 200:
		if not json_data['data']['createTeam']['ok']:
			click.echo('\n' + json_data['data']['createTeam']['error']['message'] + '\n')
		else:
			click.echo('\nThe group "%s" has been successfully created in your Marvel account\n' % name)
	else:
		click.echo("\nTry 'marvelcli create-group --help' to make sure you are not missing any args.\n")

@click.option('-g', '--group-pk', type=int, help='Pk of the group you want to add members to')
@click.option('-e', '--email', type=str, multiple=True, help='Use this flag for each email address you want added to your group')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def add_members_to_group(group_pk: int, email: list, auth: str):
	"""Add members to a group"""
	params = {'teamPk': group_pk,'emails': email}
	query = group_queries.add_members_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		if not group_pk:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			click.echo(json_data['data']['addMembersToTeam']['error']['message'])
	else:
		if not email:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			data_success = json_data['data']['addMembersToTeam']['succeeded']
			data_failed = json_data['data']['addMembersToTeam']['failed']
			if data_success:
				successful_emails = []
				for s in data_success:
					successful_emails.append(s.get('email'))

				click.echo("\nThe following people were successfully added to group %s: %s" % (group_pk, ', '.join(successful_emails)))

			if data_failed:
				click.echo('\nThe following people could not be added to group %s for the following reasons:' % (group_pk))
				for f in data_failed:
					click.echo("%s  - %s" % (f.get('email'), f.get('message')))

			click.echo("\n")

@click.option('-g', '--group-pk', type=int, help='Pk of the group you want to remove members from')
@click.option('-e', '--email', type=str, multiple=True, help='Use this flag for each email address you want removed from your group')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def remove_members_from_group(group_pk: int, email: list, auth: str):
	"""Remove members from a group"""
	params = {'teamPk': group_pk,'emails': email}
	query = group_queries.remove_members_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		if not group_pk:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			click.echo(json_data['data']['removeMembersFromTeam']['error']['message'])
	else:
		if not email:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			data_success = json_data['data']['removeMembersFromTeam']['succeeded']
			data_failed = json_data['data']['removeMembersFromTeam']['failed']

			if data_success:
				click.echo("\nThe following people were successfully removed from group %s: %s" % (group_pk, data_success))

			if data_failed:
				click.echo('\nThe following people could not be removed from group %s:' % (group_pk))
				for f in data_failed:
					click.echo("%s  - %s" % (f.get('email'), f.get('message')))

			click.echo("\n")

@click.option('-g', '--group-pk', type=int, help='Pk of the group you want to update the name for')
@click.option('-n', '--name', type=str, help='New name for your group')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def update_group_name(group_pk: int, name: str, auth: str):
	"""Update a group name"""
	params = {'pk': group_pk, 'name': name}
	query = group_queries.update_group_name_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code == 200:
		if not json_data['data']['updateGroup']['ok']:
			click.echo('\n' + json_data['data']['updateGroup']['error']['message'])
		else:
			click.echo("\nThe name of the group was updated successfully to '%s'\n" % name)
	else:
		click.echo("\nTry 'marvelcli update_group_name --help' to make sure you are not missing any args.\n")
