#!/usr/bin/python3
# A Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request


if __name__ == "__main__":
    try:
        url = "https://alx-intranet.hbtn.io/status"
        with urllib.request.urlopen(url) as response:
            output = response.read()

            print("Body response:")
            print("    - type:", type(output))
            print("    - content:", output)
            print("    - utf8 content:", output.decode('utf-8'))
    except urllib.error.URLError as e:
        print("An Error occurred:", e)
