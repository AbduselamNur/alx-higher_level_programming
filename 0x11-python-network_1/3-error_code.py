#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            output = response.read().decode('utf-8')
            print(output)
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
