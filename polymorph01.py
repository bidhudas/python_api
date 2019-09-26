#!/usr/bin/python3

class Bear(object):
    def sound(self):
        print("Grrrrooooooaaaaaarrrrr")

class Dog(object):
    def sound(self):
        print("Woooofff woooffff wuuuuffffff")

def makeSound(animalType):
    animalType.sound()

bearObj = Bear()
dogObj = Dog()

#dogObj.sound()
#bearObj.sound()

makeSound(dogObj)
makeSound(bearObj)
