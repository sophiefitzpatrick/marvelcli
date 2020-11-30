# from setuptools import setup

setup(
    name="marvel-cli",
    version="0.1",
    author='Sophie Fitzpatrick',
   	author_email='sophierfitzpatrick@gmail.com',
    packages=["cliproject"],
    install_requires=['click', 'requests'],
    entry_points={
        "console_scripts": [
            "marvel-cli = cliproject.__main__:main"
        ]
    },
)
