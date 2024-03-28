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
        url = sys.argv[1]
        try:
            with urllib.request.urlopen(url) as response:
                request_id = response.getheader('X-Request-Id')
                if request_id:
                    print(request_id)
                else:
                    print("No X-Request-Id header found in the response.")
        except urllib.error.URLError as e:
            print(f"An error occurred: {e.reason}")
