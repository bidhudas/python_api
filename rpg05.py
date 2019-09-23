#!/usr/bin/python3

def showInstructions():
    print('''
    RPG GAME
    -------
    Commands:
     go [direction]
     get [direction]
    ''')

def showStatus():
    print('------------------------')
    print('You are in the', currentRoom)
    print('Inventory:', str(inventory))
    if "item" in rooms[currentRoom]:
        print("You see a", rooms[currentRoom]['item'])
    print('------------------------')

inventory = []

rooms = {
        'Hall': {
            'south': 'Kitchen',
            'east': 'Dining Room',
            'item': 'cookies'
            },
        'Kitchen': {
            'north': 'Hall',
            'item': 'monster'
            },
        'Dining Room': {
            'west': 'Hall'
            }
        }

currentRoom = 'Hall'

showInstructions()

## Start a forever loop
while True:
    showStatus()

    move = ''

    while move == '':
        move = input('> ')

    # go sOutH
    # Get CaRRot
    move = move.lower().split()
    # ['go', 'south']
    # ['get', 'carrot']

    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You cannot go that way!")

        if currentRoom == "Dining Room":
            print("You found the dining room! Great job! Sit down and eat. You win!")
            break

    if "item" in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'cookies' in inventory:
            print("The monster steals your cookies and runs away!")
            inventory.remove('cookies')
            del rooms[currentRoom]['item']
        else:
            print("The monster eats you! GAME OVER!")
            break

    if move[0] == "get":
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print("You picked up", move[1])
            del rooms[currentRoom]['item']
        else:
            print("You cannot pickup", move[1])
