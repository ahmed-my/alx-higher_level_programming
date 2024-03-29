#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API
to display your id
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]

    url = "https://api.github.com/user"
    response = get(url, auth=(username, password))
    json = response.json()

    print(json.get('id'))
