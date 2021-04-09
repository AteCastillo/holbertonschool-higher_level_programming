#!/usr/bin/python3
'''same as task 2'''


import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    new = {'email': argv[2]}
    x = requests.post(url, data=new)
    print(x.text)
