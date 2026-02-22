#Author:Jenna Robbins
#Course: CS499
#Date : February 2026
#Enhanced Text Based Adventure Game

from collections import deque  # deque allows O(1) queue operations for efficient BFS

# Rooms are modeled as a graph using an adjacency list.
# Each room is a node, and each direction is an edge.
rooms = {
    'Entrance': {
        'neighbors': {'north': 'Hallway'},  # Connected room
        'item': None
    },
    'Hallway': {
        'neighbors': {'south': 'Entrance', 'east': 'Kitchen', 'west': 'Library'},
        'item': None
    },
    'Kitchen': {
        'neighbors': {'west': 'Hallway'},
        'item': 'Flashlight'
    },
    'Library': {
        'neighbors': {'east': 'Hallway', 'north': 'Bedroom'},
        'item': 'Key'
    },
    'Bedroom': {
        'neighbors': {'south': 'Library'},
        'item': 'Map'
    },
    'Basement': {
        'neighbors': {},
        'item': 'Zombies'
    }
}


def bfs_find_nearest_item(start_room, collected_items):
    visited = set()  # Prevents revisiting rooms (avoids cycles)
    queue = deque([(start_room, [start_room])])  # Stores (room, path_taken)

    while queue:
        current_room, path = queue.popleft()  # O(1) removal from front

        if current_room in visited:
            continue

        visited.add(current_room)

        # If room has an uncollected item (excluding Zombies), return shortest path
        if rooms[current_room]['item']:
            item = rooms[current_room]['item']
            if item != 'Zombies' and item not in collected_items:
                return path  # BFS guarantees shortest path in unweighted graph

        # Add neighboring rooms to queue for exploration
        for neighbor in rooms[current_room]['neighbors'].values():
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # No remaining items found


def give_hint(current_room, inventory):
    path = bfs_find_nearest_item(current_room, inventory)

    if path and len(path) > 1:
        print("\nShortest path to next uncollected item:")
        print(" -> ".join(path))
    else:
        print("No remaining items found or you're already in an item room.")


def main():
    current_room = 'Entrance'
    inventory = []  # Tracks collected items

    print("Welcome to the Adventure Game!")
    print("Collect all items before encountering Zombies.")
    print("Available commands: go [direction], get [item], hint, quit")
    print("Directions: North, South, East, West")

    while True:
        print("\nYou are in the", current_room)

        if rooms[current_room]['item']:
            print("You see:", rooms[current_room]['item'])

        command = input("\nEnter command: ").strip().lower()

        if command == "quit":
            print("Thanks for playing!")
            break

        elif command == "hint":
            give_hint(current_room, inventory)  # Uses BFS to assist player

        elif command.startswith("go "):
            direction = command.split()[1]

            # Navigation now uses graph lookup instead of static conditionals
            if direction in rooms[current_room]['neighbors']:
                current_room = rooms[current_room]['neighbors'][direction]

                # Win/Lose condition check
                if rooms[current_room]['item'] == 'Zombies':
                    if len(inventory) == 3:
                        print("You defeated the Zombies! You win!")
                    else:
                        print("You encountered Zombies without all items. Game Over.")
                    break
            else:
                print("You can't go that way.")

        elif command.startswith("get "):
            item = command.split()[1].capitalize()

            # Constant-time lookup of room item
            if rooms[current_room]['item'] == item:
                inventory.append(item)
                rooms[current_room]['item'] = None  # Remove item after pickup
                print(item, "collected!")
            else:
                print("Item not found in this room.")

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()