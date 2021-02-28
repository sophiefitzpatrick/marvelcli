import click
import json

from marvelcli import utils
from marvelcli.project import project_queries
from marvelcli.workspace import workspace_queries

@click.option('-p', '--project-pk', type=str, help='Pk of the project you want to delete')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def delete_project(project_pk: str, auth: str):
	"""Delete a project"""
	params = {'pk': project_pk}
	query = project_queries.delete_project_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code == 200:
		if json_data['data']['deleteProject'] is None:
			click.echo("\nProject '%s' has not been deleted for the following reason: %s\n" % (
				project_pk,
				json_data['errors'][0]['message']
			))
		else:
			click.echo("\n'%s' has been successfully deleted from your Marvel account\n" % project_pk)
	else:
		click.echo("\nTry 'marvelcli delete_project --help' to make sure you are not missing any args.\n")

@click.option('-p', '--project-pk', type=int, help='Pk of the project you want to add groups to')
@click.option('-g', '--group-pk', type=int, multiple=True, help='Use this flag for each group you want added to your project')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def add_groups_to_project(project_pk: int, group_pk: list, auth: str):
	"""Add groups to a project"""
	params = {'projectPk': project_pk,'teamPks': group_pk}
	query = project_queries.add_groups_to_project_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		if not project_pk or not group_pk:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			click.echo('\n' + json_data['data']['addTeamsToProject']['error']['message'] + '\n')
	else:
		data_success = json_data['data']['addTeamsToProject']['succeeded']
		data_failed = json_data['data']['addTeamsToProject']['failed']

		if data_success:
			successful_groups = []
			for s in data_success:
				successful_groups.append(s.get('pk'))
			click.echo("\nThe following groups were successfully added to project %s: %s \n" % (project_pk, successful_groups))

		if data_failed:
			click.echo('\nThe following groups could not be added to project %s:' % (project_pk))
			for f in data_failed:
				click.echo("%s  - %s" % (f.get('teamPk'), f.get('message')))

		click.echo("\n")

@click.option('-p', '--project-pk', type=int, help='Pk of the project you want to remove groups from')
@click.option('-g', '--group_pk', type=int, multiple=True, help='Use this flag for each group you want removed from your project')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def remove_groups_from_project(project_pk: int, group_pk: list, auth: str):
	"""Remove groups from a project"""
	params = {'projectPk': project_pk,'teamPks': group_pk}
	query = project_queries.remove_groups_from_project_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		if not project_pk or not group_pk:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			click.echo('\n' + json_data['data']['removeTeamsFromProject']['error']['message'] + '\n')
	else:
		data_success = json_data['data']['removeTeamsFromProject']['succeeded']
		data_failed = json_data['data']['removeTeamsFromProject']['failed']

		if data_success:
			successful_groups = []
			for s in data_success:
				successful_groups.append(s.get('pk'))
			click.echo("\nThe following groups were successfully removed from project %s: %s\n" % (project_pk, successful_groups))

		if data_failed:
			click.echo('\nThe following groups could not be removed from project %s:' % (project_pk))
			for f in data_failed:
				click.echo("%s  - %s" % (f.get('teamPk'), f.get('message')))

		click.echo("\n")

@click.option('-p', '--project-pk', type=int, help='Pk of the project you want to add collaborators to')
@click.option('-e', '--email', type=str, multiple=True, help='Use this flag for each email address you want added to your project')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def add_collabs_to_project(project_pk: int, email: list, auth: str):
	"""Add collaborators to a project"""
	params = {'projectPk': project_pk,'emails': email}
	query = project_queries.add_collabs_to_project_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		if not project_pk:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			click.echo('\n' + json_data['data']['addCollaboratorsToProject']['error']['message'] + '\n')
	else:
		# status_code 200 without all args
		if not email:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			data_success = json_data['data']['addCollaboratorsToProject']['succeeded']
			data_failed = json_data['data']['addCollaboratorsToProject']['failed']

			if data_success:
				successful_emails = []
				for s in data_success:
					successful_emails.append(s.get('email'))
				click.echo("\nThe following people were successfully added to project %s: %s" % (project_pk, ', '.join(successful_emails)))

			if data_failed:
				click.echo('\nThe following people could not be added to project %s for the following reasons:' % (project_pk))
				for f in data_failed:
					click.echo("%s  - '%s'" % (f.get('email'), f.get('message')))

			click.echo("\n")


@click.option('-p', '--project-pk', type=int, help='Pk of the project you want to remove collaborators from')
@click.option('-e', '--email', type=str, multiple=True, help='Use this flag for each email address you want removed from your project')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def remove_collabs_from_project(project_pk: int, email: list, auth: str):
	"""Remove collaborators from a project"""
	params = {'projectPk': project_pk,'emails': email}
	query = project_queries.remove_collabs_from_project_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		if not project_pk:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			click.echo('\n' + json_data['data']['removeCollaboratorsFromProject']['error']['message'] + '\n')
	else:
		if not email:
			click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
		else:
			data_success = json_data['data']['removeCollaboratorsFromProject']['succeeded']
			if json_data['data']['removeCollaboratorsFromProject']['succeeded']:
				click.echo("\nThe following people were successfully removed from project %s: %s" % (project_pk, data_success))

			data_failed = json_data['data']['removeCollaboratorsFromProject']['failed']
			if data_failed:
				click.echo('\nThe following people could not be removed from project %s for the following reasons:' % (project_pk))
				for f in data_failed:
					click.echo("%s  - '%s'" % (f.get('email'), f.get('message')))

			click.echo("\n")


@click.option('-n', '--name', type=str, help='Name of project')
@click.option('-pw', '--password', type=str, help='Project password')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def create_project(name: str, password: str, auth: str):
	"""Create a new project"""
	if not name:
		click.echo("\nLooks like you might be missing some args, add `--help` to your command to see the options.\n")
	else:
		user_query = workspace_queries.get_billing_info_query
		req, json_data_user = utils.make_request(auth, user_query)
		plan = json_data_user['data']['user']['company']['billing']['plan']['title']
		proj_used = json_data_user['data']['user']['company']['billing']['projectQuantityUsed']
		if plan == 'Free' and proj_used == 1:
			click.echo("\nYou have maxed out your allowances, either delete a project then run the command again or upgrade for unlimited projects: https://marvelapp.com/plans \n")
		else:
			params = {'name': name,'password': password}
			if not password:
				params['password'] = ''
			query = project_queries.create_project_query
			r, json_data = utils.make_request(auth, query, params)

			if r.status_code != 200:
				click.echo('\n' + 'A new project could not be created at this time."' + '\n')
			else:
				click.echo('\n"%s" has been successfully created in your Marvel account \n' % name)

@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def get_personal_projects(auth: str):
	"""List all projects owned by you"""
	query = project_queries.get_all_personal_projects_query
	r, json_data = utils.make_request(auth, query)

	if r.status_code != 200:
		click.echo('\n' + 'Your personal projects could not be returned at this time."' + '\n')
	else:
		data = json_data['data']['user']['projects']['edges']
		urls = []
		for d in data:
			url = d['node']['prototypeUrl']
			urls.append(url)

		project_count = len(json_data['data']['user']['projects']['edges'])
		click.echo('\nYou have %s project(s):' % project_count)

		for url in urls:
			click.echo(url)

		click.echo("\n")
