#!/usr/bin/python3
'''to fetch an url'''
import urllib3.request

with urllib3.request.urlopen('https://intranet.hbtn.io/status') as response:
   html = response.read()
print(type(html))
print(html)
print(html.decode())
