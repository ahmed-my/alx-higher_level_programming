#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = get(url)
    json = response.json()

    count = 1
    for elem in json:
        if count > 10:
            break
        sha = elem.get('sha')
        author = elem.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        count += 1
