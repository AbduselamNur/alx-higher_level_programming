#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    output = req.text
    print("Body response:")
    print("\t- type: {}".format(type(output)))
    print("\t- content: {}".format(output))
