# from setuptools import setup, find_packages

# setup(
#     name='marvelcli',
#     version='0.1',
#     packages=find_packages(),
#     include_package_data=True,
#     install_requires=[
#         'Click',
#     ],
#     entry_points='''
#         [console_scripts]
#         marvelcli=marvelcli.scripts.marvelcli:cli
#     ''',
# )

from setuptools import setup

setup(
    name='marvelapp-cli',
    version='0.1',
    py_modules=['marvelcli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        marvelcli=marvelcli:marvelcli
    ''',
)


import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="marvelapp-cli",
    version="0.0.1",
    author="Sophie Fitzpatrick",
    author_email="sophierfitzpatrick@gmail.com",
    description="A CLI wrapper for Marvelapp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sophiefitzpatrick/marvelcli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        marvelcli=marvelcli.marvelcli:marvelcli
    ''',
)