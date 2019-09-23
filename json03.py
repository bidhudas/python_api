#!/usr/bin/python3

import json

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}, {"name": "Marvin the paranoid android", "species": None}]

    print(hitchhikers)

    with open("guide.galaxy", "w") as guide:
        # json.dump creates a FILE
        json.dump(hitchhikers, guide)


    print("--------")
    print(type(hitchhikers))

    myjson = json.dumps(hitchhikers)

    print(type(myjson))

    print(hitchhikers[1])
    print(myjson[1])

main()
