#!/usr/bin/python3
"""
The first argument will be the repository name
The second argument will be the owner name
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    username = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)
    req = requests.get(url)
    json = req.json()
    try:
        for i in range(10):
            commit = json[i]
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author))
    except IndexError:
        pass
