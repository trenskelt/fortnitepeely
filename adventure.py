"""A tiny Fortnite adventure starring Peely."""

rooms = {
    "camp": {"exits": ["forest", "tower"], "items": []},
    "forest": {"exits": ["camp", "bunker"], "items": ["battery", "fuel"]},
    "tower": {"exits": ["camp"], "items": ["lens"]},
    "bunker": {"exits": ["forest", "rocket"], "items": ["keycard"]},
    "rocket": {"exits": ["bunker"], "items": []},
}
room, bag = "camp", []
powered = unlocked = fueled = done = False
tries = 0


def look():
    print(f"\nPeely is at the {room}. Exits: {', '.join(rooms[room]['exits'])}")
    print("Items:", ", ".join(rooms[room]["items"]) or "none")


def command(text):
    global room, powered, unlocked, fueled, done, tries
    words = text.lower().split()
    if not words:
        return
    verb, item = words[0], " ".join(words[1:])
    if verb in ("help",):
        print("Commands: look, go <place>, take <item>, use <item>, inv, answer <number>, quit")
    elif verb == "look":
        look()
    elif verb == "inv":
        print("Inventory:", ", ".join(bag) or "empty")
    elif verb == "go" and item in rooms[room]["exits"]:
        if item == "rocket" and not unlocked:
            print("The bunker hatch is locked.")
        else:
            room = item
            look()
    elif verb == "take" and item in rooms[room]["items"]:
        rooms[room]["items"].remove(item)
        bag.append(item)
        print("Taken:", item)
    elif verb == "use" and item in bag:
        if item == "lens":
            print("Clue: 11 + 17 + 21")
        elif room == "bunker" and item == "keycard":
            unlocked = True
            print("The hatch unlocks.")
        elif room == "rocket" and item == "battery":
            powered = True
            print("Rocket powered.")
        elif room == "rocket" and item == "keycard" and powered:
            unlocked = True
            print("Launch controls unlocked.")
        elif room == "rocket" and item == "fuel" and powered and unlocked:
            fueled = True
            print("Rocket fueled. Enter the clue's total!")
        else:
            print("That won't help here.")
    elif verb == "answer":
        if room != "rocket" or not (powered and unlocked and fueled):
            print("Get the rocket ready first.")
        elif len(words) < 2 or not words[1].isdigit():
            print("Enter a number.")
        else:
            tries += 1
            if int(words[1]) == 49:
                print("Peely blasts away from the storm. You win!")
                done = True
            elif tries == 3:
                print("The storm catches Peely. Game over.")
                done = True
            else:
                print(f"Wrong! {3 - tries} tries left.")
    elif verb == "quit":
        print("Peely didn't escape the storm.")
        done = True
    else:
        print("Try 'help' or check the room.")


def main():
    global done
    print("PEELY'S FORTNITE ESCAPE: outrun the storm!")
    look()
    while not done:
        command(input("> "))


if __name__ == "__main__":
    main()