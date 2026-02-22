#Author:Jenna Robbins
#Course: CS140
#Date : December 2023

def show_instructions():
    print("Zombie Text Adventure Game")
    print('')
    print("Collect 6 items to win the game, or be eaten by the Zombies.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("Type 'quit' to end the game")
    print('')

rooms = {
    'Mud Room' : {'East': 'Living Room' , 'South': 'Hallway' , 'item': 'Shoes'},
    'Living Room' : {'West': 'Mud Room' , 'item': 'Zombies'},
    'Hallway' : {'North': 'Mud Room' , 'South': 'Bedroom' , 'East': 'Family Room' , 'West': 'Garage'},
    'Garage' : {'East': 'Hallway' , 'item': 'Vest'},
    'Bedroom' : {'North': 'Hallway' , 'East': 'Basement' , 'item': 'Gun'},
    'Basement' : {'West': 'Bedroom' , 'item': 'Notepad'},
    'Family Room' : {'West': 'Hallway' , 'North': 'Kitchen' , 'item': 'Crowbar'},
    'Kitchen' : {'South': 'Family Room' , 'item': 'Knife'}
}

def move_room(direction, current_room):
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print("You can't go that way!")
        return current_room

show_instructions()

stop = False
current_room = 'Mud Room'
inventory = []

while not stop:
    print(f'You are in the {current_room}')
    print(f'Inventory: {inventory}')
    print('-------------------')

    if 'item' in rooms[current_room]:
        print(f'You see a {rooms[current_room]["item"]}')

    user_input = input('Enter a command: ')

    if user_input == 'quit':
        stop = True
    elif user_input.startswith('go '):
        direction = user_input.split(' ')[1].capitalize()
        current_room = move_room(direction, current_room)
    elif user_input.startswith('get '):
        item = user_input.split(' ')[1].capitalize()
        if 'item' in rooms[current_room] and rooms[current_room]['item'] == item:
            print(f'You have collected the {item}.')
            inventory.append(item)
            del rooms[current_room]['item']
        else:
            print(f'There is no {item} in this room.')
    else:
        print('Invalid command. Try again.')

    if len(inventory) == 6:
        print("Congratulations! You have collected all items and killed the zombies!")
        stop = True
    elif current_room == 'Living Room':
        print("The Zombies ate you!... GAME OVER!")
        stop = True

print("Thanks for playing the game! Hope you enjoyed it!")