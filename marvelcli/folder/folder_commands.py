import click

from marvelcli import utils
from marvelcli.folder import folder_queries

# Limited by the API to only be able to create folders at the moment.

@click.option('-n', '--name', type=str, help='Name of folder')
@click.option('-v', '--visibility', type=str, help='`workspace` by default, use this flag with `private` for a private folder ')
@click.option('-a', '--auth', type=str, help='Auth your request')
@click.command()
def create_folder(name: str, visibility: str, auth: str):
	"""Create a folder"""
	if not visibility:
		visibility = 'WORKSPACE'
	params = {'name': name, 'visibility': visibility.upper()}
	query = folder_queries.create_folder_query
	r, json_data = utils.make_request(auth, query, params)

	if r.status_code == 200:
		if not json_data['data']['createFolder']['ok']:
			click.echo('\n' + json_data['data']['createFolder']['error']['message'] + '\n')
		else:
			click.echo('\nThe %s folder "%s" has been successfully created in your Marvel account\n' % (visibility.lower(), name))
	else:
		click.echo("\nTry 'marvelcli create-folder --help' to make sure you are not missing any args.\n")
