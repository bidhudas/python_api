#!/usr/bin/python3
"""Rzfeeser@alta3.com || best practice"""

import yaml

def main():
    """run time code"""
    with open("datacenter.yaml", "r") as yammy:
        pyyam = yaml.load(yammy)
    pyyam["row7"] = ['lucky1', 'lucky2']
    with open("datacenterimp.yaml", "w") as yammy:
        yaml.dump(pyyam, yammy)

if __name__ == "__main__":
    main()
