'''
Let's allow the player to sell apples at the town.
Let's add more stuff to buy in the town. A sword, a shield, an amulet
'''

# Spooky Forest Adventure - Full Updated Version

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
        "exits": {"west": "crossroads"},
        "spooky_event_done": False,
        "blocked_by_ghost": True
    },
    "town": {
        "description": (
            "You enter a bustling town full of colorful shops and people chatting in the streets.\n"
            "A vendor calls out: 'Enchanted Water Wings (3 gold), Sword (5 gold), Shield (4 gold), Amulet (7 gold)!'\n"
            "(Type 'buy [item]' to purchase or 'sell apple' to sell apples.)"
        ),
        "exits": {"south": "crossroads"},
        "vendor_items": {
            "water wings": 3,
            "sword": 5,
            "shield": 4,
            "amulet": 7
        }
    }
}

inventory = []
gold = 5
current_room = "spooky_forest"

print("Welcome to the Spooky Forest Adventure!")
print("You start with 5 gold.")
print("Type 'go [direction]', 'look', 'inventory', 'take [item]', 'buy [item]', 'sell apple', or 'quit'.\n")

while True:
    room = rooms[current_room]

    # Lake ghost encounter
    if current_room == "lake" and room.get("blocked_by_ghost", False):
        if "water wings" not in inventory:
            print(room["description"])
            print("\nA ghostly figure rises from the mist and blocks your path!")
            print('"Only those with enchanted water wings may pass..." 👻')
            print("You feel an invisible force preventing you from going further.")
            # Bounce player back to crossroads
            current_room = "crossroads"
            continue
        else:
            if not room.get("spooky_event_done"):
                print(room["description"])
                print("\nThe ghost rises again—but upon seeing your water wings, it bows silently and vanishes into the mist.")
                room["spooky_event_done"] = True
                room["blocked_by_ghost"] = False
            else:
                print(room["description"])
    else:
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
        print(f"Gold: {gold}")
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
    elif command.startswith("buy "):
        item = command[4:]
        if current_room == "town":
            vendor = rooms["town"].get("vendor_items", {})
            if item in vendor:
                price = vendor[item]
                if gold >= price:
                    if item in inventory:
                        print(f"You already have {item}.")
                    else:
                        inventory.append(item)
                        gold -= price
                        print(f"You buy the {item} for {price} gold.")
                else:
                    print("You don't have enough gold.")
            else:
                print("There's nothing like that for sale here.")
        else:
            print("There's no vendor here to buy from.")
    elif command.startswith("sell "):
        item = command[5:]
        if current_room == "town":
            if item == "apple":
                if inventory.count("apple") > 0:
                    inventory.remove("apple")
                    gold += 2
                    print("You sell an apple for 2 gold.")
                else:
                    print("You don't have any apples to sell.")
            else:
                print(f"You can't sell {item} here.")
        else:
            print("There's no vendor here to sell to.")
    elif command.startswith("go "):
        direction = command[3:]
        if direction in room["exits"]:
            current_room = room["exits"][direction]
        else:
            print("You can't go that way.")
    else:
        print("I don't understand that command.")

    print()
