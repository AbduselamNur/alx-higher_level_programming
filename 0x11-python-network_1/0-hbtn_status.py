#!/usr/bin/python3
# A Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        output = response.read()

        print("Body response:")
        print("    - type:", type(output))
        print("    - content:", output)
        print("    - utf8 content:", output.decode('utf8'))
