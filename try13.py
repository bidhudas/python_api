#!/usr/bin/python3

while True:
    try:
        print("We should div x by y!")
        x = int(input("What is the value of x? "))
        y = int(input("What is the value of y? "))
        print(f'The product of {x} / {y} is ', x/y, sep="--------->")
    except ZeroDivisionError:
        print("You cannot div anything by 0! Restarting...")
    except ValueError:
        print("You seem to be giving me something other than arithmatic values! Restaring...")
    except:
        print("I have no CLUE what you were trying to do... but it doesn't seem to compute! Restarting...")

