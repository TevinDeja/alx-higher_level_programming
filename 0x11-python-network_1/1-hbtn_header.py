#!/usr/bin/python3
"""
script that takes in a URL
sends a request to the URL
displays the value of the X-Request-Id variable found in the header of response.
"""
import urllib.request
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.getheader('X-Request-Id'))
