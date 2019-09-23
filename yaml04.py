#!/usr/bin/python3

import yaml

def main():
    with open("datacenter.yaml", "r") as yammy:
        pyyam = yaml.load(yammy)

    pyyam["row7"] = ['lucky1', 'lucky2']

    with open("datacenterimp.yaml", "w") as yammy:
        yaml.dump(pyyam, yammy)

    #print(pyyam)

main()
