# marvelcli

A CLI wrapper for Marvelapp (https://marvelapp.com)

The wrapper will enable you to interact with your Marvel
account from the comfort of your command line.

To auth each command you'll need to use the `-a` flag with
your access token.

You can generate a new one or find the one you have
already set up here: https://marvelapp.com/oauth/devtoken

## Getting started:

`pip install marvelapp-cli`

https://pypi.org/project/marvelapp-cli/

## Example:

To create a project:

	marvelcli create-project --name Rua --password floof --auth [your access token]

## Commands available:

You can find out how to use each command with:

	marvelcli [command name] --help

	Command Name:                Command Use:

	about-user                   User statistics
	add-collabs-to-project       Add collaborators to a project
	add-groups-to-project        Add groups to a project
	add-members-to-group         Add members to a group
	bulk-transfer-projects	     Bulk transfer projects within your workspace
	create-folder                Create a folder
	create-group                 Create a group
	create-project               Create a new project
	delete-groups                Delete groups
	delete-project               Delete a project
	get-billing-info             Get billing information
	get-personal-projects        List all projects owned by you
	invite-users-to-workspace    Invite users to your workspace
	remove-collabs-from-project  Remove collaborators from a project
	remove-groups-from-project   Remove groups from a project
	remove-members-from-group    Remove members from a group
	remove-users-from-workspace  Remove users from your workspace
	update-account-password      Update your account password
	update-group-name            Update a group name
	update-user                  Update your email, username and occuption

## Coming soon:

1. Auth the entire session
2. Command grouping
3. Comment, screen, usertest commands
