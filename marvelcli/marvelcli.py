#!/usr/bin/env python3
import click
import json
import datetime

from marvelcli import utils
from marvelcli.user import user_commands
from marvelcli.workspace import workspace_commands
from marvelcli.project import project_commands
from marvelcli.folder import folder_commands
from marvelcli.group import group_commands

@click.group()
def marvelcli(args=None):
    """A CLI wrapper for Marvelapp

	The wrapper will enable you to interact with your Marvel
	account from the comfort of your command line.

	To auth each command you'll need to use the -a flag with
	your access token key.

	You can generate a new one here or find the one you
	already have set up: https://marvelapp.com/oauth/devtoken

	"""

# User
marvelcli.add_command(user_commands.update_account_password)
marvelcli.add_command(user_commands.update_user)
marvelcli.add_command(user_commands.about_user)

# Workspace
marvelcli.add_command(workspace_commands.get_billing_info)
marvelcli.add_command(workspace_commands.remove_users_from_workspace)
marvelcli.add_command(workspace_commands.invite_users_to_workspace)

# Project
marvelcli.add_command(project_commands.delete_project)
marvelcli.add_command(project_commands.create_project)
marvelcli.add_command(project_commands.add_groups_to_project)
marvelcli.add_command(project_commands.remove_groups_from_project)
marvelcli.add_command(project_commands.add_collabs_to_project)
marvelcli.add_command(project_commands.remove_collabs_from_project)
marvelcli.add_command(project_commands.get_personal_projects)
marvelcli.add_command(project_commands.bulk_transfer_projects)

# Group
marvelcli.add_command(group_commands.delete_groups)
marvelcli.add_command(group_commands.create_group)
marvelcli.add_command(group_commands.add_members_to_group)
marvelcli.add_command(group_commands.remove_members_from_group)
marvelcli.add_command(group_commands.update_group_name)

# Folder - limited by the API
marvelcli.add_command(folder_commands.create_folder)


if __name__ == "__main__":
    marvelcli()
