# Spooky Forest Adventure with Inventory

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
        "description": "You walk into open farm country. Apple trees line the edge of the fields. You can try to 'take apple' here.",
        "exits": {"east": "crossroads"},
        "item": "apple",
        "item_taken": False
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

inventory = []
current_room = "spooky_forest"

print("Welcome to the Spooky Forest Adventure!")
print("Type 'go [direction]', 'look', 'inventory', 'take [item]', or 'quit'.\n")

while True:
    room = rooms[current_room]
    print(room["description"])
    
    command = input("\nWhat do you want to do? ").lower().strip()
    
    if command == "quit":
        print("Thanks for playing!")
        break
    elif command == "look":
        print(room["description"])
    elif command == "inventory":
        if inventory:
            print("You are carrying:", ", ".join(inventory))
        else:
            print("You are not carrying anything.")
    elif command.startswith("take "):
        item = command[5:]
        if "item" in room and room["item"] == item and not room.get("item_taken", False):
            inventory.append(item)
            room["item_taken"] = True
            print(f"You take the {item}.")
        elif "item" in room and room["item"] == item:
            print(f"You already took the {item}.")
        else:
            print("There is nothing like that here.")
    elif command.startswith("go "):
        direction = command[3:]
        if direction in room["exits"]:
            current_room = room["exits"][direction]
        else:
            print("You can't go that way.")
    else:
        print("I don't understand that command.")
    
    print()
