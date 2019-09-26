#!/usr/bin/python3

#imports

class Dog: # create the dog class
    def __init__(self, name, age): # define the attributes name and age
        self.nm = name
        self.yrs = age

    def __str__(self):
        return f'{self.nm} {self.yrs}'

    def aged(self, yearsolder):
        self.yrs = self.yrs + yearsolder

    def newname(self, nname):
        self.nm = nname

class Working(Dog):
    def __init__(self, name, age, isHunter):
        Dog.__init__(self, name, age)
        self.ishunt = isHunter

    def __str__(self):
        return f'{self.nm} {self.yrs} {self.ishunt}'

    def trained(self, istrained):
        self.ishunt = istrained

def main():
    sparky = Dog("Benji", 3)

    print(sparky)

    sparky.newname("Larry")

    print(sparky)

    sparky.aged(10)

    print(sparky)

    ## subclassing
    mix = Working("Oscar", 10, True)

    print(mix)

    mix.aged(2)

    mix.trained(False)

    print(mix)

if __name__ == "__main__":
    main()
