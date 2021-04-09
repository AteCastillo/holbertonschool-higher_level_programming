#!/usr/bin/python3
'''http error'''

import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            page = response.read()
        print(page.decode())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
