#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data={'q':  q})

    try:
        json = req.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
