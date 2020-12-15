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
