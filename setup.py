from setuptools import setup

setup(
    name="marvelcli",
    version="0.1",
    author='Sophie Fitzpatrick',
   	author_email='sophierfitzpatrick@gmail.com',
    packages=["cliproject"],
    install_requires=['click', 'requests'],
    entry_points={
        "console_scripts": [
            "marvelcli = cliproject.__main__:main"
        ]
    },
)
