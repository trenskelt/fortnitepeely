"""A Fortnite adventure starring Peely."""

rooms = {
    "camp": ["forest", "tower"],
    "forest": ["camp", "bunker"],
    "tower": ["camp"],
    "bunker": ["forest", "rocket"],
    "rocket": ["bunker"],
}
items = {"forest": ["battery", "fuel"], "tower": ["lens"], "bunker": ["keycard"]}
room, bag = "camp", []
powered = hatch_open = controls_ready = fueled = done = False
tries = 0

print("PEELY'S FORTNITE ESCAPE: outrun the storm!")
while not done:
    print(f"\nAt {room}. Exits: {', '.join(rooms[room]) or 'none'}")
    print("Items:", ", ".join(items.get(room, [])) or "none")
    words = input("> ").lower().split()
    if not words:
        continue
    verb, target = words[0], " ".join(words[1:])

    if verb == "help":
        print("Commands: go <place>, take <item>, use <item>, inv, answer <number>, quit")
    elif verb == "inv":
        print("Inventory:", ", ".join(bag) or "empty")
    elif verb == "go":
        if target == "rocket" and not hatch_open:
            print("The bunker hatch is locked.")
        elif target in rooms[room]:
            room = target
        else:
            print("You can't go there.")
    elif verb == "take" and target in items.get(room, []):
        items[room].remove(target)
        bag.append(target)
        print("Taken:", target)
    elif verb == "use" and target in bag:
        if target == "lens":
            print("Clue: 11 + 17 + 21")
        elif room == "bunker" and target == "keycard":
            hatch_open = True
            print("The bunker hatch unlocks.")
        elif room == "rocket" and target == "battery":
            powered = True
            print("Rocket powered.")
        elif room == "rocket" and target == "keycard" and powered:
            controls_ready = True
            print("Launch controls unlocked.")
        elif room == "rocket" and target == "fuel" and powered and controls_ready:
            fueled = True
            print("Rocket fueled. Enter the clue's total!")
        else:
            print("That won't help here.")
    elif verb == "answer":
        if room != "rocket" or not (powered and controls_ready and fueled):
            print("Get the rocket ready first.")
        elif len(words) < 2 or not words[1].isdigit():
            print("Enter a number.")
        else:
            tries += 1
            if int(words[1]) == 49:
                print("Peely escapes the storm. You win!")
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
