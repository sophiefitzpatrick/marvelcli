import click
import json

import utils
from project import project_queries

@click.option('-p', '--project-pk', type=str, help='Pk of the project you want to delete')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def delete_project(project_pk: str, auth: str):
	"""Delete a project"""
	params = {'pk': project_pk}
	query = project_queries.delete_project_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code == 200:
		if not json_data['data']['deleteproject']['ok']:
				click.echo('\n' + json_data['data']['deleteproject']['error']['message'] + '\n')
		else:
			click.echo('\n"%s" has been successfully deleted from your Marvel account\n' % pk)
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
		click.echo('\n' + json_data['data']['addTeamsToProject']['error']['message'] + '\n')
	else:
		data_success = json_data['data']['addTeamsToProject']['succeeded']
		data_failed = json_data['data']['addTeamsToProject']['failed']

		if data_success:
			successful_groups = []
			for s in data_success:
				successful_groups.append(s.get('pk'))
			click.echo("\nThe following groups were successfully added to project %s: %s " % (project_pk, successful_groups))

		if data_failed:
			click.echo('\nThe following groups could not be added to project %s:' % (project_pk))
			for f in data_failed:
				click.echo("%s  - %s \n" % (f.get('teamPk'), f.get('message')))

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
		click.echo('\n' + json_data['data']['removeTeamsFromProject']['error']['message'] + '\n')
	else:
		data_success = json_data['data']['removeTeamsFromProject']['succeeded']
		data_failed = json_data['data']['removeTeamsFromProject']['failed']

		if data_success:
			successful_groups = []
			for s in data_success:
				successful_groups.append(s.get('pk'))
			click.echo("\nThe following groups were successfully removed from project %s: %s" % (project_pk, successful_groups))

		if data_failed:
			click.echo('\nThe following groups could not be removed from project %s:' % (project_pk))
			for f in data_failed:
				click.echo("%s  - %s \n" % (f.get('teamPk'), f.get('message')))

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
		click.echo('\n' + json_data['data']['addCollaboratorsToProject']['error']['message'] + '\n')
	else:
		data_success = json_data['data']['addCollaboratorsToProject']['succeeded']
		data_failed = json_data['data']['addCollaboratorsToProject']['failed']

		if data_success:
			successful_emails = []
			for s in data_success:
				successful_emails.append(s.get('email'))
			click.echo("\nThe following people were successfully added to project %s: %s" % (pk, ', '.join(successful_emails)))

		if data_failed:
			click.echo('\nThe following people could not be added to project %s:' % (pk))
			for f in data_failed:
				click.echo("%s  - '%s' \n" % (f.get('email'), f.get('message')))


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
		click.echo('\n' + json_data['data']['removeCollaboratorsFromProject']['error']['message'] + '\n')
	else:
		if json_data['data']['removeCollaboratorsFromProject']['succeeded']:
			click.echo("\nThe following people were successfully removed from project %s: %s" % (pk, ', '.join(data_success)))

		data_failed = json_data['data']['removeCollaboratorsFromProject']['failed']
		if data_failed:
			click.echo('\nThe following people could not be removed from project %s:' % (pk))
			for f in data_failed:
				click.echo("%s  - '%s' \n" % (f.get('email'), f.get('message')))


@click.option('-n', '--name', type=str, help='Name of project')
@click.option('-pw', '--password', type=str, help='Project password')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def create_project(name: str, password: str, auth: str):
	"""Create a new project"""
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
	data = json_data['data']['user']['projects']['edges']

	urls = []
	for d in data:
		url = d['node']['prototypeUrl']
		urls.append(url)

	project_count = len(json_data['data']['user']['projects']['edges'])
	click.echo('\nYou have %s project(s)' % project_count)

	for url in urls:
		click.echo(url)

@click.option('-p', '--project-pk', type=int, multiple=True, help='Use this flag for each project pk you want transferred')
@click.option('-e', '--email', type=str, help='The email of the person recieving the projects, make sure they are in the same workspace as you')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def bulk_transfer_projects(email: str, auth: str, project_pk: list):
	"""Bulk transfer projects within your workspace"""
	params = {'userEmail': email,'projectPks': project_pk}
	query = project_queries.bulk_transfer_project_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code != 200:
		click.echo('\n' + json_data['data']['bulkTransferProjects']['error']['message'] + '\n')
	else:
		data_success = json_data['data']['bulkTransferProjects']['succeeded']
		data_failed = json_data['data']['bulkTransferProjects']['failed']

		if data_success:
			click.echo("\nThe following projects were successfully transferred to %s: %s \n" % (email, data_success))

		if data_failed:
			click.echo('\nThe following projects were not successfully transferred to %s: ' % (email))
			for f in data_failed:
				click.echo("%s  - %s \n" % (f.get('projectPk'), f.get('message')))

