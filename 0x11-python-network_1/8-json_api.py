#!/usr/bin/python3
'''takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=data)
    try:
        json_response = response.json()
        if len(json_response) == 0:
            print("No result")
        else:
            print("[{}] {}"
                  .format(json_response.get("id"),
                          json_response.get("name")))
    except:
        print("Not a valid JSON")
