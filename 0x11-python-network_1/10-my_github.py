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

    url = 'https://api.github.com/user'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        user_data = response.json()
        print(user_data.get('id'))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
