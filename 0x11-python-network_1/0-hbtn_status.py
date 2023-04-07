#!/usr/bin/python3
# A Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        output = response.read()

        print("Body response:")
        print("    - type: {}".format(type(output)))
        print("    - content: {}".format(output))
        print("    - utf8 content: {}".format(output.decode('utf-8')))
