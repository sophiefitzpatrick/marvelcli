# marvelcli

A CLI wrapper for Marvelapp (https://marvelapp.com)

The wrapper will enable you to interact with your Marvel
account from the comfort of your command line.

## Getting started:

`pip install marvelapp-cli`

https://pypi.org/project/marvelapp-cli/

## Authing requests:

You will need an access token to use the CLI, generate a new one or find the one you already have set up here: https://marvelapp.com/oauth/devtoken

You can export your token by running this command from the same dir you installed the CLI:
`export MARVEL_CLI_TOKEN='your access token'`

The CLI will then automatically use this token for each command you run (so you don't have to auth each one individually).

To unauth:
`unset MARVEL_CLI_TOKEN`

## Example:

To invite users to your workspace:

	marvelcli add-collabs-to-project --project 12345 --email "janis@bigbrotherandtheholdingcompany.com" --email "stevie@fleetwoodmac.com" --email "grace@jeffersonairplane.com"

## Commands available:

You can find out how to use each command with:

	marvelcli [command name] --help

	Command Name:                Command Use:

	about-user                   User statistics
	add-collabs-to-project       Add collaborators to a project
	add-groups-to-project        Add groups to a project
	add-members-to-group         Add members to a group
	create-folder                Create a folder
	create-group                 Create a group
	create-project               Create a new project
	delete-groups                Delete groups
	delete-project               Delete a project
	get-billing-info             Get billing information
	get-personal-projects        List all projects owned by you
	remove-collabs-from-project  Remove collaborators from a project
	remove-groups-from-project   Remove groups from a project
	remove-members-from-group    Remove members from a group
	remove-users-from-workspace  Remove users from your workspace
	update-group-name            Update a group name

## Feature requests

Anything you'd like to see that isn't here?
Email sophierfitzpatrick@gmail.com with your request!
