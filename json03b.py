#!/usr/bin/python3
"""RZFeeser@alta3.com || reading in JSON files"""

import json

def main():
    # open up datacenter.json
    with open("datacenter.json", "r") as datacenter:
        dcj = datacenter.read()

    #print(dcj['row1'])
    print(type(dcj))

    # convert datacenter.json to pythonic data
    pydcj = json.loads(dcj)
    print(type(pydcj))
    print(pydcj["row1"])

    # print out the contents of each row key-- devote one line to each row

main()

