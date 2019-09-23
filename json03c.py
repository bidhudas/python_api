#!/usr/bin/python3
"""RZFeeser@alta3.com || reading in JSON files"""

import json

def main():
    # open up datacenter.json
    with open("datacenter.json", "r") as datacenter:
        pydcj = json.load(datacenter)

    print(pydcj["row1"])
    print(type(pydcj))

main()

