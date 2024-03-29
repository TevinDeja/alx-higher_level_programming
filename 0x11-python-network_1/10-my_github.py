#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, token))
    if r.status_code == 200:
        print(r.json().get('id'))
    else:
        print(None)
