#!/usr/bin/python3
'''same as task 1'''

import requests
import sys


if __name__ == "__main__":
    page = requests.get(sys.argv[1])
    print(page.headers.get['X-Request-Id'])
