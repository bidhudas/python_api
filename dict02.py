#!/usr/bin/python3

def main():
    hostipdict = {"host01":"10.10.2.3", "host02":"10.0.1.1", "host03":"72.5.4.22"}
    
    hostipdict['host04'] = "192.168.1.1"
    
    print(hostipdict)

    print(hostipdict["host02"])

    # this line causes a KEY ERROR
    try:
        print("This will work, no mention of wing commander")
        #print(hostipdict['fakekey'])
    except:
        print("Thank you for playing wing commander!")

    #if hostipdict.get("hostz"):
    #    print("Wow that value did exist!")
    #else:
    #    print("Couldn't find that brother")

    print("Some critical line of code")

    print(hostipdict.keys())

    print(hostipdict.values())

    print(hostipdict)

    employees = {"max": 16, "names": [{"first": "Jerry", "last": "Springer"}, {"first": "Terry", "last": "Scary"}, {"first": "William", "last": "Riker"}, {"first": "Harry", "last": "Potter"}], "campus": "building5"}

    print((employees.get("names"))[2].get("last"))


    for x in employees.get("names"):
        #print(x.values())
        #print( x.get("first"), x.get("last") )
        #print( x.get("first") + " " + x.get("last") )
        print( x["first"] + " " + x["last"] )





main()
