#!/usr/bin/python3
'''
Zach Feeser | rzfeeser@alta3.com
demo the requests library
'''

# python3 -m pip install requests
import requests

# creating an object called astros by making an HTTP request with GET
astros = requests.get('http://api.open-notify.org/astros.json')

# display to screen 
print((astros.json()).get('people'))

for astro in (astros.json()).get('people'):
    print(astro['name'].split()[1])

## print(dir(astros))
