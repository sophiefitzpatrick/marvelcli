# marvelcli

November 2020

A CLI wrapper for Marvelapp (https://marvelapp.com)

The wrapper will enable you to interact with your Marvel
account from the comfort of your command line.

To auth each command you'll need to use the -a flag with
your access token.

You can generate a new one or find the one you have
already set up here: https://marvelapp.com/oauth/devtoken

## example

To create a project:

	marvel-cli create-project -n Rua -p floof -a [your access token]
