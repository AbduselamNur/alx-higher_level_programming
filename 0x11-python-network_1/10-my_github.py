#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    req = requests.get("https://api.github.com/user", auth=(username, pwd))
    json = req.json()
    print(json.get("id"))
