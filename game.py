from player import *
from items import *
from gameparser import *
from time import *
from map import *
import time
import msvcrt
import sys
import banner

cameras = 6
guards = 6

def calculate_carry_mass(inventory):
    """"""

    carry_mass=0
    for item in inventory:
        carry_mass += item_index[item]["mass"]
    return carry_mass


def list_of_items(item_list):
    """
    """
    global items
    item_string=""
    for item in item_list:
        item_name = item_index[item]["name"]
        item_string="{0}, {1}".format(item_string,item_name)
    item_string =item_string[2:]

    return item_string


def print_room_items(room):
    """
    """
    if room["contents"]!= []:
        print("There is {0} here.\n".format(list_of_items(room["contents"])))


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

    return locations[exits[direction]]["name"]


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
       for act in item_index[room_item]["action"]:
             print(act.upper() + " " + item_index[room_item]["name"].upper() + " to " + act.lower() + " " + item_index[room_item]["name"])

    for inv_item in inv_items:
        print(item_index[inv_item]["undo_action"].upper() + " " + item_index[inv_item]["name"].upper() + " to " + item_index[inv_item]["undo_action"].lower() + " " + item_index[inv_item]["name"])
    if current_room["name"] == "Toilets" and ("laptop" in inventory):
        print("CONNECT LAPTOP to connect your laptop to the toilet Wi-Fi...")
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """
    """
    return chosen_exit in exits


def execute_go(direction):
    """ """
    global current_room
    global suspicion

    if is_valid_exit(current_room["exits"],direction):
        if (current_room["exits"][direction]) == "Security Office":
            if "keycard" in inventory:
                current_room=move(current_room["exits"],direction)
                print("You open the door with the keycard.")
            else:
                print("The door is locked.")
        elif (current_room["exits"][direction]) == "Vault":
            if (cameras == 0 and guards == 0):
                current_room=move(current_room["exits"],direction)
                print("You enter the vault room, the disabled cameras allow you to remain hidden.")
                print("It seems that none of the guards heard you...")
                return
            else:
                if (cameras > 0):
                    print("Oh no! The cameras have spotted you!")
                if (guards > 0):
                    print("Uh-oh, a guard was patrolling and spotted you!")
                suspicion = 10
        else:
            current_room=move(current_room["exits"],direction)
    else:
        print("You cannot go there.")


def execute_interact(item_id):
    """
    """

    print("item id is " + item_id)
    global current_room
    global inventory
    global current_carry_mass
    inv_changed=False
    for item in current_room["contents"]:
        if item_id in item:
            if current_carry_mass + item_index[item]["mass"] < 3:
                inventory.append(item)
                current_room["contents"].remove(item)
                inv_changed=True
                current_carry_mass = calculate_carry_mass(inventory)
            else:
                print("That is too heavy")
    if not(inv_changed):
        print("You cannot do that.")


def execute_drop(item_id,current_room):
    for item in locations[current_room]:
        if item_id in item:
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
        if (item_id in item_index[item]["id"].lower()):
            current_room["contents"].append(item)
            inventory.remove(item)
            inv_changed=True
            current_carry_mass = calculate_carry_mass(inventory)
    if not(inv_changed):
        print("You cannot drop that.")

def execute_interact_command(command):
    if len(command) > 1:
        execute_interact(command[1])
    else:
        print("Take what?")
def execute_go_command(command):
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

def execute_vent_command(command):
    if len(command) > 1 and command[1] == "vent":
        if command[0] == "unscrew":
            print("You unscrew the vent and climb inside and end up at the...")
            item_vent["action"] = "Climb through"
        else:
            print("You climb inside and end up at the...")
        current_room = location_managers
    else:
        print("Unscrew what?")

def execute_punch_command(command):
    global suspicion
    if len(command) > 1 and (command[1] == "security" or command[2] == "guard"):
        suspicion = suspicion + 1
        print("\"What are you doing!?\"")
        print("Suspicion levels are now at: " + str(suspicion))

def execute_bribe_command(command):
    global suspicion
    if len(command) > 1 and (command[1] == "security" or command[2] == "guard"):
        valid_offer = False
        print("What are you offering?")
        for item in inventory:
            print("Offer " + item_index[item]["name"] + ".")
        offer = input("I will give you my: ")
        for item in inventory:
            if offer.lower() in item_index[item]["name"].lower():
                valid_offer = True
                offer = item_index[item]["id"]
        if valid_offer:
            if offer in[ "lunchcoupon" ,"donuts" ] :
                print("This is exactly what I needed. Thanks!")
                print("I will tell the other guards to go on break.")
                guards = 0
                for key, room in locations.items():
                    if "securityguard" in room["contents"]:
                        room["contents"].remove("securityguard")
                inventory.remove(offer)
            else:
                print("Erm...I don't want this.")
                suspicion = suspicion + 1
                print("Suspicion levels are now at: " + str(suspicion))
        else:
            print("What? I don't even know what you just said.")
            suspicion += 1
            print("Suspicion levels are now at: " + str(suspicion))

def execute_deactivate_command(command):
    global cameras
    if (cameras == 0):
        print("You've already deactivated all the cameras.")
        return
    else:
        cameras = 0
        for key, room in locations.items():
            if "securitycamera" in room["contents"]:
                room["contents"].remove("securitycamera")
        print("You deactivated all the camera's in the bank!")

def execute_cut_command(command):
    global cameras
    if len(command) > 1 and (command[1] == "security" or command[2] == "cameras"):
        if "wirecutters" in inventory:
            current_room["contents"].remove("securitycamera")
            cameras = cameras - 1
            print("You cut the camera.")
            print(str(cameras) + " cameras remain in the bank...")
        else:
            print("You try to cut the cable with your hand. It fails to cut.")
            return
def execute_apologise_command(command):
    global suspicion
    if len(command) > 1 and (command[1] == "security" or command[2] == "guard"):
        if suspicion > 0:
            suspicion = suspicion - 1
        print("\"Don't worry about it.\"")
        print("Suspicion levels are now at: " + str(suspicion))
def execute_drop_command(command):
    if len(command) > 1:
        execute_drop(command[1])
    else:
        print("Drop what?")
def execute_inspect_command(command):
    if len(command) > 1:
        execute_drop(command[1])
    else:
        print("inspect what?")

def execute_save_command(command):
    create_save()

def execute_load_command(command):
    load_save()
def execute_connect_command(command):
    global suspicion
    if command[1] == "laptop":
        print("You attempt to connect your Laptop to the Wi-Fi...")
        print("...Connected")
        print("What do you want to do: ")
        print("HACK CAMERAS to attempt to hack the bank's cameras.")
        print("SOUND ALARMS to sound the bank's alarms.")
        choice = input()

        if ("hack" in choice and "camera" in choice):
            hacked = False
            hackp = 30
            multiplier = 12.00
            print("Press ENTER quickly to hack!")
            wait = input("PRESS ENTER TO START")
            while hacked == False:
                time_start = time.time()
                bufferE = input().lower()
                time_taken = time.time()
                hackp = hackp - int((time_taken-time_start)*multiplier)
                hackp = hackp + 2
                #delete_last_lines()
                for _ in range(1, hackp):
                    print("|", end="")
               # sleep(0.2)
                if hackp > 45:
                    hacked = True
                    print("\nYou did it! You hacked the cameras!")
                    cameras = 0
                    for key, room in locations.items():
                        if "securitycamera" in room["contents"]:
                            room["contents"].remove("securitycamera")

                    print("Type EXIT to close the laptop.")
                    while(bufferE != "exit"):
                        bufferE = input().lower()
                    return
                elif hackp <= 0:
                    print("You failed to hack the cameras. Security noticed the strange activity on the network.")
                    suspicion = suspicion + 1
                    print("Suspicion levels are at: " + str(suspicion))
                    print("Type EXIT to close the laptop.")
                    while(bufferE != "exit"):
                        bufferE = input().lower()
                    return

                multiplier = multiplier + 1
                if multiplier > 40:
                    multiplier = 5
        elif ("sound" in choice and "alarm" in choice):
            suspicion = 10
            print("Why did you do that...")
            return
    else:
        print("connect to what?")
def execute_command(command):
    """
    """
    global current_room
    global suspicion
    global cameras
    global guards

    command_dict={
        "go":execute_go_command,
        "take": execute_interact_command,
        "steal": execute_interact_command,
        "pick": execute_interact_command,
        "wear":execute_interact_command,
        "drink":execute_interact_command,
        "unscrew": execute_vent_command,
        "climb": execute_vent_command,
        "punch": execute_punch_command,
        "bribe": execute_bribe_command,
        "deactivate": execute_deactivate_command,
        "apologise": execute_apologise_command,
        "drop": execute_drop_command,
        "inspect": execute_inspect_command,
        "save": execute_save_command,
        "load": execute_load_command,
        "connect": execute_connect_command,
    }

    if 0 == len(command):
        return
    if command[0] in command_dict:
        command_dict[command[0]](command)
    #VAULT HANDLING
    elif current_room["name"] == "Vault":
        if command[0] == "use" and command[1] == "drill":
            if "drill" in inventory:
                print("You manage to unscrew the bolts on the door, removing the metal frame.")
                print("The base of the door collapses and makes a loud noise.")
                suspicion = suspicion + 1
                current_room["contents"].remove("vault")
                current_room["contents"].append("gold")
            else:
                print("You start drilling the door with your hand.")
                print("Nothing happens.")
        if command[0] == "enter" and command[1] == "combination":
            combination = input("Enter the vault combination: ")
            if (combination == "0000"):
                print("Success! The door silently swings open.")
                current_room["contents"].remove("vaultdoor")
                current_room["contents"].append("gold")
            else:
                print("That was the wrong code! The alarms sound and security rush the room.")
                suspicion = 100
    else:
        print("This makes no sense.")

def delete_last_lines(n=1):
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def menu(exits, room_items, inv_items):
    """"""

    print_menu(exits, room_items, inv_items)

    user_input = input("> ")

    normalised_user_input = normalise_input(user_input)

   # bs code to test print("normalised: " + normalised_user_input[0] + normalised_user_input[1] + normalised_user_input[2])
    return normalised_user_input


def move(exits, direction):
    """"""

    return locations[exits[direction]]


# ----------------------------------------------- #
# ---------------- pre-game part ---------------- #
# ----------------------------------------------- #


def pregame():
    """
    rough structure

        Print title screen DONE

        dialougue

        manager stuff

        Store stuff (append to inventory)



    """
    banner.game_banner()
    #time.sleep(2)

    #pregame_dialogue() #BE AWARE this may be a python file to import.
    #pre_game_bar()

    #time.sleep(3)
    #pregame_dialogue() #BE AWARE this may be a python file to import.
  #  pre_game_shop()

    #pre_game_home()

    print("And so the heist begins") #PLACEHOLDER, just needs something to say its moving to game proper



def main():

    won = False
    pregame()
    global current_room
    global current_carry_mass
    global suspicion

    suspicion = 0
    current_room= locations["Lobby"]
   # inventory= player.inventory
    current_carry_mass = calculate_carry_mass(inventory)


    while not (won):
        #print(current_room)
        if (suspicion > 2):
            print("\n\n\n\nYOU DIED\n\n\n\n")
            return
        print_room(current_room)
        print_inventory_items(inventory)
        #print("Your current carry weight is {}kg. \n".format(current_carry_mass))
        command = menu(current_room["exits"], current_room["contents"], inventory)

        execute_command(command)

    print("\n\nCongrats!")


#Save Bank Heist game

def load_save():
    global current_room
    global cameras
    global suspicion
    global guards
    
    data_reading = ""
    room = ""

    #with open("save.txt", "r") as text_file:

    lines = open("save.txt").read().splitlines()

    #print(lines)

    del inventory[:]
    for key, room in locations.items():
        room["contents"] = [] #deleting old

    for line in lines:
        if (line != ""):
            if line == "~ INVENTORY ~":
               # print("reading inv")
                data_reading = line
                continue
            elif line == "~ MAP ~":
                #print("reading map")
                data_reading = line
                continue
            elif line == "~ CURRENT LOCATION ~":
               # print("reading location")
                data_reading = line
                continue
            elif line == "~ SUSPICION ~":
                data_reading = line
                continue
            elif line == "~ CAMERAS ~":
                data_reading = line
                continue
            elif line == "~ GUARDS ~":
                data_reading = line
                continue

            if data_reading == "~ INVENTORY ~":
                #print("writing inv")
                inventory.append(line)
            elif data_reading == "~ MAP ~":
                #print("writing map")
                if "#" in line:
                    print("stripping")
                    room = line.strip('#')
                    continue
                else:
                    locations[room]["contents"].append(line)
            elif (data_reading == "~ CURRENT LOCATION ~"):
                current_room = locations[line]
            elif (data_reading == "~ SUSPICION ~") :
                suspicion = int(line)
                data_reading = ""
            elif (data_reading == "~ CAMERAS ~") :
                cameras = int(line)
                data_reading = ""
            elif (data_reading == "~ GUARDS ~") :
                guards = int(line)
                data_reading = ""
                #print("current  room changed")
    print("Loaded Succesfully.")



def create_save():
    with open("save.txt", "w") as new_save:
        new_save.write("~ INVENTORY ~" + "\n")
        for item in inventory:
            new_save.write(item + "\n")

        new_save.write("\n\n")
        new_save.write("~ MAP ~" + "\n\n")
        for key, room in locations.items():
            new_save.write("#" + room["name"] + "\n")
            for items in room["contents"]:
                new_save.write(items + "\n")
            new_save.write("\n")
        new_save.write("~ CURRENT LOCATION ~" + "\n\n")
        new_save.write(current_room["name"] + "\n\n")
        new_save.write("~ SUSPICION ~" + "\n")
        new_save.write(str(suspicion) + "\n")
        new_save.write("~ CAMERAS ~" + "\n")
        new_save.write(str(cameras) + "\n")
        new_save.write("~ GUARDS ~" + "\n")
        new_save.write(str(guards))
        print("Saved Succesfully.")
    #new_save.close()



if __name__ == "__main__":
    main()


