#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    response = get(url)
    print(response.text)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
