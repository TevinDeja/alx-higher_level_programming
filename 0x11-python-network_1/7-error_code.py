#!/usr/bin/python3
"""
script that takes in a URL
sends a request to the URL and displays the body of the response.
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            response = requests.get(url)
            response.raise_for_status()
            print(response.text)
        except requests.exceptions.HTTPError as e:
            print(f"Error code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
