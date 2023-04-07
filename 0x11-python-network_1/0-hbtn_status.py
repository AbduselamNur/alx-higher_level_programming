#!/usr/bin/python3
# A Python script that fetches https://alx-intranet.hbtn.io/status
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        output = response.read()

        print("Body response:")
        print("\t- type:", type(output))
        print("\t- content:", output)
        print("\t- utf8 content:", output.decode('utf-8'))
