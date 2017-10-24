#!/usr/bin/python3

import map
import player
import items
import banner
import gameparser
import time



def calculate_carry_mass(inventory):
    """"""

    carry_mass=0
    for item in inventory:
        carry_mass += item["mass"]
    return carry_mass


def list_of_items(item_list):
    """
    """
    item_string=""
    for item in item_list:
        item_name=items.items[item]["name"]
        item_string="{0}, {1}".format(item_string,item_name)
    item_string =item_string[2:]

    return item_string


def print_room_items(room):
    """
    """
    if room["contents"]!= []:
        print( "There is {0} here.\n".format(list_of_items(room["contents"])))


def print_inventory_items(items):
    """
    """
    print("You have {0}.\n".format(list_of_items(items)))


def print_room(room):
    """
    """
    #print(room)
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    print_room_items(room)

def exit_leads_to(exits, direction):
    """
    """
    return map.areas[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """

    """
    print("You can:")
    for direction in exits:

        print_exit(direction, exit_leads_to(exits, direction))

    for room_item in room_items:
        #print(room_item)
       # print(items.items[room_item]["id"].upper()+ ":" + room_item["name"])
        print("TAKE {0} to take {1}.".format(items.items[room_item]["id"].upper(),items.items[room_item]["name"] ))

    for inv_item in inv_items:
        print("DROP {0} to drop your {1}.".format(inv_item["id"].upper(),inv_item["name"] ))

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """
    """
    return chosen_exit in exits


def execute_go(direction):
    """ """
    global current_room

    if is_valid_exit(current_room["exits"],direction):
        current_room=move(current_room["exits"],direction)
    else:
        print("You cannot go there.")


def execute_take(item_id):
    """
    """
    global current_room
    global inventory
    global current_carry_mass
    inv_changed=False
    for item in current_room["items"]:
        if item_id == item["id"]:
            if current_carry_mass+ item["mass"]<3:
                inventory.append(item)
                current_room["items"].remove(item)
                inv_changed=True
                current_carry_mass = calculate_carry_mass(inventory)
            else:
                print("That is too heavy")
    if not(inv_changed):
        print("You cannot take that.")


def execute_drop(item_id,current_room):
    for item in map.areas[current_room]:
        if item==item_id:
            print(item["Description"])
        else:
            print("You cannot inspect that")

def execute_drop(item_id):
    """"""
    global current_room
    global inventory
    global current_carry_mass
    inv_changed=False
    for item in inventory:
        if item_id == item["id"]:
            current_room["items"].append(item)
            inventory.remove(item)
            inv_changed=True
            current_carry_mass = calculate_carry_mass(inventory)
    if not(inv_changed):
        print("You cannot drop that.")


def execute_command(command):
    """
    """
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    elif command[0] == "inspect":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("inspect what?")
    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """"""

    print_menu(exits, room_items, inv_items)

    user_input = input("> ")

    normalised_user_input = gameparser.normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """"""

    return map.areas[exits[direction]]

def pregame_dialogue():
    """
    prints the pregame dialogue



    """
    print("PLACEHOLDER. This will be dialogue someday")

def pregame_shop():
    print("PLACEHOLDER. This will be a shop someday")

def pregame():
    """
    rough structure

        Print title screen DONE

        dialougue

        manager stuff

        Store stuff (append to inventory)



    """
    banner.game_banner()
    #time.sleep(3)
    pregame_dialogue() #BE AWARE this may be a python file to import.
    pregame_shop()
    print("And so the heist begins") #PLACEHOLDER, just needs something to say its moving to game proper



def main():

    won=False
    pregame()
    global current_room
    current_room=map.areas["Lobby"]
    inventory= player.inventory
    while not (won):
        #print(current_room)
        print_room(current_room)
        print_inventory_items(inventory)
        #print("Your current carry weight is {}kg. \n".format(current_carry_mass))
        command = menu(current_room["exits"], current_room["contents"], inventory)

        execute_command(command)

    print("\n\nCongrats!")


if __name__ == "__main__":
    main()

