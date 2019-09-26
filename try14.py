#!/usr/bin/python3

import uuid

ticket = uuid.uuid4()
x = ""

while True:
    try:
        print("Type the name of the config file to load into the switch: ")
        configfile = input("Filename: ")
        with open(configfile, 'r') as configfileobj:
            swithconfig = configfileobj.read()
    except:
        pass

#    except Exception as err:
#        x = f'There was a problem... {err}'
#        exit()
    else:
        x = f'The file {configfile} successfully harvested!'
        break
    finally:
        if not x:
            x = "there was a problem..."
        with open("tryexcept.log", "a") as log:
            print("writing results to log file")
            print(f"{ticket} - {x}", file=log)

try:
    print("I want to get the product of 10 / ?: ")
    x = input("Set a value of ? ")
    print(10 / int(x))
except:
    print("That does not compute")

print("thanks for using this program")
