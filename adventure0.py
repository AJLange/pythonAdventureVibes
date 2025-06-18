'''
I really like text adventures. how would I go about creating one of those?
Let's build the game in python.
The game starts lost in a spooky forest, and then the player can go north to a crossroads. From the roads they can go west, to farm country, east, to the lake, or north, to a bustling town full of shopping. 
'''

# Spooky Forest Text Adventure Game

rooms = {
    "spooky_forest": {
        "description": "You are lost in a dark, spooky forest. The wind howls through the trees. A narrow path leads north.",
        "exits": {"north": "crossroads"}
    },
    "crossroads": {
        "description": "You stand at a lonely crossroads. Signs point west to farmland, east to a lake, and north to a bustling town.",
        "exits": {"south": "spooky_forest", "west": "farm_country", "east": "lake", "north": "town"}
    },
    "farm_country": {
        "description": "You walk into open farm country. The smell of hay and soil fills the air.",
        "exits": {"east": "crossroads"}
    },
    "lake": {
        "description": "You arrive at a quiet lake. Mist hovers over the water. It feels... unsettling.",
        "exits": {"west": "crossroads"}
    },
    "town": {
        "description": "You enter a bustling town full of colorful shops and people chatting in the streets.",
        "exits": {"south": "crossroads"}
    }
}

current_room = "spooky_forest"

print("Welcome to the Spooky Forest Adventure!")
print("Type 'go [direction]', 'look', or 'quit' to play.\n")

while True:
    room = rooms[current_room]
    print(room["description"])
    
    command = input("\nWhat do you want to do? ").lower().strip()
    
    if command == "quit":
        print("Thanks for playing!")
        break
    elif command.startswith("go "):
        direction = command[3:]
        if direction in room["exits"]:
            current_room = room["exits"][direction]
        else:
            print("You can't go that way.")
    elif command == "look":
        print(room["description"])
    else:
        print("I don't understand that command.")
    
    print()
