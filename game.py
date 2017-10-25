#!/usr/bin/python3

import map
from player import *
from items import *
import banner
import time



def calculate_carry_mass(inventory):
    """"""

    carry_mass=0
    for item in inventory:
        carry_mass += item["mass"]
    return carry_mass


def list_of_items(items):
    """
    """
    item_string=""
    for item in items:
        item_name=item["name"]
        item_string="{0}, {1}".format(item_string,item_name)
    item_string =item_string[2:]

    return item_string


def print_room_items(room):
    """
    """
    if room["items"]!= []:
        print( "There is {0} here.\n".format(list_of_items(room["items"])))


def print_inventory_items(items):
    """
    """
    print("You have {0}.\n".format(list_of_items(items)))


def print_room(room):
    """
    """

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
        print("TAKE {0} to take {1}.".format(room_item["id"].upper(),room_item["name"] ))

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

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """"""

    print_menu(exits, room_items, inv_items)

    user_input = input("> ")

    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """"""

    return map.areas[exits[direction]]


# ----------------------------------------------- #
# ---------------- pre-game part ---------------- #
# ----------------------------------------------- #
def pre_game_print_option(location):
    # print the option the player can choice
    print("Which of the following action will you take?")
    for i in range()
    '''
    print("Which of the following action will you take? (Please input as a integer!)")
    for i in range(len(location["question"])):
        print(str(i + 1) + ") " + location["question"][i] + " (" + location["hints"][i] + ")")
    
    print()
    '''


def pre_game_read_user_input(option):
    user_input = input("> ")


def pre_game_cal_budget(balance, value):
    # cal_budget(balance, )
    amount = balance - value
    if amount >= 0:
        return amount
    else:
        return False


def change_status()



def pre_game_bar():
    # print("") <-- print the story
    pre_game_print_option(location_bar)
        

def pre_game_shop():
    # print("") <-- print the story
    pre_game_print_option(location_shop)


def pre_game_home():
    # print("") <-- print the story
    pre_game_print_option(location_home)


def pregame():
    """
    rough structure

        Print title screen DONE

        dialougue

        manager stuff

        Store stuff (append to inventory)



    """
    banner.game_banner()
    time.sleep(3)
    #pregame_dialogue() #BE AWARE this may be a python file to import.
    #pregame_shop()
    print("And so the heist begins") #PLACEHOLDER, just needs something to say its moving to game proper



def main():

    won = False
    pregame()
    while not (won):

        print_room(current_room)
        print_inventory_items(inventory)
        print("Your current carry weight is {}kg. \n".format(current_carry_mass))
        command = menu(current_room["exits"], current_room["items"], inventory)

        execute_command(command)

    print("\n\nCongrats!")


if __name__ == "__main__":
    main()

