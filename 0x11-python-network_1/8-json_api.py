#!/usr/bin/python3
"""A script that takes in a letter and sends a Post request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from requests import post
from sys import argv


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    response = post(url, data)

    response_type = response.headers['content-type']

    if response_type == 'application/json':
        result = response.json()
        id_value = result.get('id')
        name = result.get('name')
        if (result != {} and id_value and name):
            print("[{}] {}".format(id_value, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
