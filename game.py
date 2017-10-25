from player import *
from items import *
from gameparser import *
from time import *
from map import *
import time
import pregame

import banner

#Global variables used to control certain conditions
cameras = 6
guards = 6
manager_locked = True
janitor_locked = True
security_locked = True
noise_level = 0

def calculate_carry_mass(inventory):
    """"""
    carry_mass=0
    for item in inventory:
        carry_mass += item_index[item]["mass"]
    return carry_mass
#Used to calculcate the current mass of the player's inventory
#Currently unused

def list_of_items(item_list):
    #Displays items in a nicely formatted list
    global items
    item_string=""
    for item in item_list:
        item_name = item_index[item]["name"]
        item_string="{0}, {1}".format(item_string,item_name)
    item_string =item_string[2:]

    return item_string


def print_room_items(room):
#Prints the items in the room using the list_of_items function
    if room["contents"]!= []:
        print("There is {0} here.\n".format(list_of_items(room["contents"])))


def print_inventory_items(items):
#Same as the above function, but with inventory items.
    print("You have {0}.\n".format(list_of_items(items)))


def print_room(room):
#Print the current rooms name, descriptions and contents. Formatted nicely.
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    print_room_items(room)

def exit_leads_to(exits, direction):
#returns the name of the exit in the direciton given
    return locations[exits[direction]]["name"]


def print_exit(direction, leads_to):
#prints the exits available in the current locations.
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
#Main menu displayed to the user.
#This functions indicates to the user what options are available to them in the current room.
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))

    for room_item in room_items:   
       for act in item_index[room_item]["action"]: #For each action in the action list, for each item.
             print(act.upper() + " " + item_index[room_item]["name"].upper() + " to " + act.lower() + " " + item_index[room_item]["name"])
       if current_room["name"] == "Toilets" and ("laptop" in inventory): #Check if player is in the toilets, if so add additional option (laptop)
        print("CONNECT LAPTOP to connect your laptop to the toilet Wi-Fi...")      
    print()
    for inv_item in inv_items: #Print inventory items.
        print(item_index[inv_item]["undo_action"].upper() + " " + item_index[inv_item]["name"].upper() + " to " + item_index[inv_item]["undo_action"].lower() + " " + item_index[inv_item]["name"])
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
#returns whether or not a valid exit exists in the direction given
    return chosen_exit in exits

def pick_lock_game(room):
    #The pick locking mini game function
    #Declare global variable so local ones are not created/accessed
    global manager_locked
    global janitor_locked #credits to RRR
    global security_locked
    global suspicion

    print("\n")
    picked = False
    print("Press ENTER every second to pick the lock.")
    print("Keep the tapping accurate to increase your chances of a successful pick.")
    print("Keep the accuracy above zero, otherwise your paperclip pick will break.\n")

    accuracy = 0.50 #Accuracy that is decremented during the game 
    attempt = 0 #attempts == pins left
    wait = input("PRESS ENTER TO START") ##buffer
    time_start = time.time() ##logs current time

    while picked == False:
        bufferE = input().lower()
        time_taken = time.time()
        diff = time_taken-time_start ##gets the difference in time between last key press (enter)

        time_start = time.time()

        accuracy = accuracy - abs(1-diff) #accuracy is decremented by the error in key press (difference from 1)
        print("Pins left: "+ str(10-attempt))
        print("Accuracy: " + str(accuracy))
        attempt = attempt + 1
       # print("Accuracy: " + accuracy)
        if (accuracy <= 0):
            print("Failure. Suspicion raised.")
            inventory.remove("paperclip")
            suspicion = suspicion + 1
            print("Suspicion level is now at: " + str(suspicion))
            picked = True
            input("Press ENTER to leave.")
            return
        elif (attempt == 11): #If last pin is reached, then minigame won.
            print("Success. Door unlocked.") #These next few if statements simply unlock the doors by setting the bools to False
            picked = True
            inventory.remove("paperclip")
            if(room == "Manager's Office"):
                manager_locked = False
                input("Press ENTER to continue.")
                return
            elif(room == "Janitors"):
                janitor_locked = False
                input("Press ENTER to continue.")
                return
            elif(room == "Security Office"):
                security_locked = False
                input("Press ENTER to continue.")
                return
    
def execute_go(direction):
    #Called when player is moving room.

    global current_room
    global suspicion
    global manager_locked
    global janitor_locked

    if is_valid_exit(current_room["exits"],direction):
        if (current_room["exits"][direction]) == "Security Office":
            if "keycard" in inventory: #If keycard is in inventory (picked from manager's office)
                current_room=move(current_room["exits"],direction) #allow entry
                print("You open the door with the keycard.")
            elif "paperclip" in inventory and security_locked: #If paper clip is in inventory 
                print("The door is locked.") #Offer the player to play the lockpicking minigame.
                print("Do you want to attempt to pick-lock it with PAPERCLIP? Y/N")
                answer = input()
                if answer.lower() == "yes" or answer.lower() == "y":
                    pick_lock_game("Security Office")
            elif security_locked == False:
                current_room=move(current_room["exits"],direction)
            else:
                print("The door is locked.")
        elif (current_room["exits"][direction]) == "Vault": #Check if cameras or guards exits.
            if (cameras == 0 and guards == 0): #IF not, then allow entry to the vault.
                current_room=move(current_room["exits"],direction)
                print("You enter the vault room, the disabled cameras allow you to remain hidden.")
                print("It seems that none of the guards heard you...")
                return
            else:
                if (cameras > 0):
                    print("Oh no! The cameras have spotted you!")
                if (guards > 0):
                    print("Uh-oh, a guard was patrolling and spotted you!")
                suspicion = 10 #Set suspicion to 10, instantly ending the game.
        elif (current_room["exits"][direction] == "Manager's Office"):
            if "paperclip" in inventory and manager_locked: #Paperclip minigame disalogue #2
                print("The door is locked.")
                print("Do you want to attempt to pick-lock it with PAPERCLIP? Y/N")
                answer = input()
                if answer.lower() == "yes" or answer.lower() == "y":
                    pick_lock_game("Manager's Office")
            elif manager_locked:
                print("The door is locked.")
            else:
                current_room=move(current_room["exits"],direction)
        elif current_room == location_managers:
            if manager_locked: #Check if the door is locked, if so open it from the inside.
                print("You unlock the door from the inside.")
                manager_locked = False
                current_room=move(current_room["exits"],direction)
            else:
                current_room=move(current_room["exits"],direction)
        elif (current_room["exits"][direction] == "Janitors"):
            if janitor_locked: #Same concept as above, but with key check in inventory.
                if "keys" in inventory:
                    janitor_locked = False
                    print("You unlock the door to the Janitors with the keys.")
                    current_room=move(current_room["exits"],direction)
                elif "paperclip" in inventory:
                    print("The door is locked.")
                    print("Do you want to attempt to pick-lock it with PAPERCLIP? Y/N")
                    answer = input()
                    if answer.lower() == "yes" or answer.lower() == "y":
                        pick_lock_game("Janitors")
                else:
                    print("The door is locked.")
            else:
                current_room=move(current_room["exits"], direction)
        else:
            current_room=move(current_room["exits"], direction)
    else:
        print("You cannot go there.")


def execute_interact(item_id):
    #Used for picking up items.
    global current_room
    global inventory
    for item in current_room["contents"]:
        if item_id in item:
            inventory.append(item)
            current_room["contents"].remove(item)

            if current_carry_mass + item_index[item]["mass"] < 3:
                inventory.append(item)
                current_room["contents"].remove(item)
                inv_changed=True
                current_carry_mass = calculate_carry_mass(inventory) ##Ammend carry mass.
            else:
                print("That is too heavy")
    if not(inv_changed):
        print("You cannot do that.")

#def execute_drop(item_id,current_room):
    #for item in locations[current_room]:
        #if item_id in item:
           # print(item["Description"])
       # else:
            #print("You cannot inspect that")

def execute_drop(item_id): 
    #Function handling item dropping
    global current_room
    global inventory
    for item in inventory:
        if (item_id in item_index[item]["id"].lower()):
            current_room["contents"].append(item)
            inventory.remove(item)
        if (item_id in item_index[item]["id"].lower()): #If the item exists within the inventory.
            current_room["contents"].append(item) #Add the item to the current rooms contents.
            inventory.remove(item) #..and remove it from your inventory.
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
    #Handles climbing through the vent in the janitor's office.
    global current_room
    if len(command) > 1 and command[1] == "vent":
        if command[0] == "unscrew" and "screwdriver" in inventory: #If unscrew keyword used and player owns screwdriver:
            print("You unscrew the vent.") #Unscrew the vent, and change the action available to the user.
            item_vent["action"] = ["Climb through"]
        elif command[0] == "climb":
            print("You climb inside and end up at the...")
            current_room = location_managers
    else:
        print("Unscrew what?")

def execute_punch_command(command):
    #Used for punching guards.
    #Has not benefits to the player, only raises suspicion.
    global suspicion
    if len(command) > 1 and (command[1] == "security" or command[1] == "guard"):
        suspicion = suspicion + 1
        print("\"What are you doing!?\"")
        print("Suspicion levels are now at: " + str(suspicion))

def execute_bribe_command(command):
    #Handles bribing guards.
    #Currently only accepted bribes are lunchcoupon and donuts.
    global suspicion
    global guards

    if len(command) > 1 and (command[1] == "security" or command[1] == "guard"): #command checking
        valid_offer = False
        print("What are you offering?")
        for item in inventory:
            print("Offer " + item_index[item]["name"] + ".") #Display items in your inventory to offer.
        offer = input("I will give you my: ")
        for item in inventory:
            if offer.lower() in item_index[item]["name"].lower():
                valid_offer = True
                offer = item_index[item]["id"]
        if valid_offer:
            if offer in[ "lunchcoupon" ,"donuts" ] :
                print("This is exactly what I needed. Thanks!") #Succesful bribe.
                print("I will tell the other guards to go on break.")
                guards = 0 #This is important, at this point the player can actually progress in the game.
                for key, room in locations.items():
                    if "securityguard" in room["contents"]:
                        room["contents"].remove("securityguard")
                inventory.remove(offer)
            else:
                print("Erm...I don't want this.") #Failed bribe.
                suspicion = suspicion + 1 #Increases suspicion.
                print("Suspicion levels are now at: " + str(suspicion))
        else:
            print("What? I don't even know what you just said.") #Another failed bribe, item not recognised.
            suspicion += 1
            print("Suspicion levels are now at: " + str(suspicion))

def execute_deactivate_command(command):
    #Function handling camera deactivation
    global cameras
    if (cameras == 0):
        print("You've already deactivated all the cameras.")
        return
    else:
        cameras = 0
        for key, room in locations.items(): #Removes any cameras from current room, 
            if "securitycamera" in room["contents"]:
                room["contents"].remove("securitycamera")
        print("You deactivated all the camera's in the bank!")

def execute_cut_command(command):
    #Handles cutting cameras manually.
    global cameras
    if len(command) > 1 and (command[1] == "security" or command[1] == "cameras"):
        if "wirecutters" in inventory: #Player MUST have wirecutters in order to do this.
            current_room["contents"].remove("securitycamera")
            cameras = cameras - 1
            print("You cut the camera.")
            print(str(cameras) + " cameras remain in the bank...")
        else:
            print("You try to cut the cable with your hand. It fails to cut.")
            return

def execute_apologise_command(command):
    #Hidden command used to apologise to card after punching them.
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
        if command[1] == "note" or command[2] == "note":
            print("The note says:")
            print("The clue is your course code.\n")
def execute_save_command(command):
    create_save()

def execute_load_command(command):
    load_save()
def execute_connect_command(command):
    #Called when connecting laptop to bathroom wifi
    #allows player to hack the cameras to disable them
    #alternative to using control panel in security office

    global suspicion
    global cameras

    if command[1] == "laptop":
        print("You attempt to connect your Laptop to the Wi-Fi...")
        print("...Connected")
        print("What do you want to do: ")
        print("HACK CAMERAS to attempt to hack the bank's cameras.")
        print("SOUND ALARMS to sound the bank's alarms.")
        choice = input()

        if ("hack" in choice and "camera" in choice): #The hacking minigame.
            hacked = False 
            hackp = 30 #Starting count for hacking representation(?)
            multiplier = 12.00 #Multiplier used to change difficult throughout game
            print("Press ENTER quickly to hack!")
            wait = input("PRESS ENTER TO START")
            while hacked == False:
                time_start = time.time() 
                bufferE = input().lower()
                time_taken = time.time()
                hackp = hackp - int((time_taken-time_start)*multiplier) #Adjust the amount of 'hack points' (hackp) to the amount of time before last press.
                hackp = hackp + 2 #Increment the hackp, player relies on this to actually reach target. This must be accumulate faster than hackp decays with time.
                #Decay is essentially controlled by enter presses.
                for _ in range(1, hackp):
                    print("|", end="")
               # sleep(0.2)
                if hackp > 45: ##TARGET reached!
                    hacked = True
                    print("\nYou did it! You hacked the cameras!")
                    cameras = 0
                    for key, room in locations.items(): #Disable all security cameras in rooms.
                        if "securitycamera" in room["contents"]:
                            room["contents"].remove("securitycamera")

                    print("Type EXIT to close the laptop.") #This is used to stop the Menu function being spammed with return/enter inputs when the target has been reached.
                    while(bufferE != "exit"):
                        bufferE = input().lower()
                    return
                elif hackp <= 0: #Failed attempt at hacking, resulting in 3 suspicion.
                    print("You failed to hack the cameras. Security noticed the strange activity on the network.")
                    suspicion = suspicion + 3
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

    command_dict={ #Dictionary used to cleanly access execute functions.
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
        "cut": execute_cut_command
    }

    if 0 == len(command):
        return
    if command[0] in command_dict:
        command_dict[command[0]](command)
    #VAULT HANDLING
    elif current_room["name"] == "Vault": #Vault room handling
        if command[0] == "use" and command[1] == "drill": #Drilling vault door (if drill owned)
            if "drill" in inventory:
                print("You manage to unscrew the bolts on the door, removing the metal frame.")
                print("The base of the door collapses and makes a loud noise.")
                suspicion = suspicion + 1 #Drilling open the vault door works...but does increase suspicion due to the sound created.
                current_room["contents"].remove("vault")
                current_room["contents"].append("gold")
            else:
                print("You start drilling the door with your hand.") #Failed drilling response
                print("Nothing happens.")
        if command[0] == "enter" and command[1] == "combination":
            combination = input("Enter the vault combination: ")
            if (combination == "1101"):
                print("Success! The door silently swings open.")
                current_room["contents"].remove("vaultdoor")
                current_room["contents"].append("gold")
            else:
                print("That was the wrong code! The alarms sound and security rush the room.") #If the wrong code is entered.
                suspicion = 100 #Supsicion is set to 100. The game ends.
    else:
        print("This makes no sense.")

def menu(exits, room_items, inv_items):
    """"""
    #Menu function used to print the menu
    #Also handles the user input

    print_menu(exits, room_items, inv_items)

    user_input = input("> ") #User input

    normalised_user_input = normalise_input(user_input) #The input is then normalised here, using functions imported from gameparser.py

    #Normalised input is then returned.
    return normalised_user_input


def move(exits, direction):
    #Returns the location in which the player will end up.
    return locations[exits[direction]]

def pregame_dialogue():
    """
    prints the pregame dialogue




    """


    banner.game_banner()
    time.sleep(2)

    #pregame.display_start_dialog()
    inventory=pregame.pre_game_shop()


    print("PLACEHOLDER. This will be dialogue someday")

def pregame_shop():
    print("PLACEHOLDER. This will be a shop someday")

def pregame_routine():
    """


    """
    banner.game_banner()

    #time.sleep(3)
    pregame_dialogue() #BE AWARE this may be a python file to import.
    pregame_shop()
    print("And so the heist begins") #PLACEHOLDER, just needs something to say its moving to game proper


    print("And so the heist begins") #PLACEHOLDER, just needs something to say its moving to game proper
    return inventory
def static_item_handle():
    #This function handles items that are your inventory, but are not interactable.

    global suspicion
    global noise_level
    if "skimask" in inventory: #If the player is wearing a ski mask
        suspicion = suspicion + 6 #They will automatically lose, as ski masks are a red flag to security.
        print("The guards notice your skimask, the tackle you to the ground.")
        inventory.remove("skimask")
    if "vodka" in inventory: #If the player is drunk..
        suspicion = 10  #They will lose automatically, you cannot rob a bank drunk.
        print("You stumble around the bank drunk. The guards escort you out.")
        inventory.remove("vodka")
    if "energydrink" in inventory: #Drinking energy drink. Does nothing.
        print("You drink your energy drink. You feel energised.")
        inventory.remove("energydrink")
    if "sneakers" not in inventory: #If the player is not wearing sneakers then
        noise_level = noise_level + 1 #the noise value is incremented every action.
        if (noise_level % 5 == 0): #increment after action
            suspicion = suspicion + (noise_level/5) #When five actions are made, the suspicion will increase.
            #This is because doing things makes noise. The 'sneak'ers stop you from making sound.
            print("You are moving around a lot and making a lot of noise.")
            print("Suspicion levels are at: " + str(suspicion))



def main():
    #Main function, called upon loading module.

    won=False #Set the game Won boolean to false, as the game has just started.
    inventory=pregame_routine() #Start pregame.
    global current_room
    global suspicion

    suspicion = 0
    current_room= locations["Lobby"] #Set the first room to lobby, the starting location.
    turns_taken=0
    while not (won): #While the game has not been won.s
        turns_taken+=1
        if (suspicion > 6):
            print("\n\n\n\nYOU WERE CAUGHT\n\n\n\n")
            input()
            return
        if ("gold" in inventory):
            print("\n\n\n\nYOU WON! THE HEIST WAS SUCCESFUL!\n\n\n\n")
            input()
            return
        static_item_handle()
        print_room(current_room)
        print_inventory_items(inventory)
        command = menu(current_room["exits"], current_room["contents"], inventory)

        execute_command(command) #Executes the command inputed by the user.

    print("\n\nCongrats!")


#Save Bank Heist game

def load_save():
    #Function that handles game saving.
    global current_room
    global cameras
    global suspicion
    global guards
    global manager_locked
    global janitor_locked
    global security_locked
    data_reading = ""
    room = ""

    #with open("save.txt", "r") as text_file:

    lines = open("save.txt").read().splitlines()

    #print(lines)

    del inventory[:]
    for key, room in locations.items():
        room["contents"] = [] #deleting old contents

    for line in lines: #This for loop iterates through all the lines in the file loaded.
        if (line != ""):
            if line == "~ INVENTORY ~": #These if blocks are checking for titles, they indicate what the next peice of data will represent.
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
            elif line == "~ MANAGER ~":
                data_reading = line
                continue
            elif line == "~ JANITOR ~":
                data_reading = line
                continue
            elif line == "~ SECURITY ~":
                data_reading = line
                continue

        #####################################

            if data_reading == "~ INVENTORY ~": #These if blocks are checking the data_reading var to determine what to var to set the line's data to.
                #print("writing inv")
                inventory.append(line)
            elif data_reading == "~ MAP ~":
                #print("writing map")
                if "#" in line:
                    #print("stripping")
                    room = line.strip('#')
                    continue
                else:
                    locations[room]["contents"].append(line)
            elif (data_reading == "~ CURRENT LOCATION ~"):
                current_room = locations[line]
            elif (data_reading == "~ SUSPICION ~") :
                suspicion = float(line)
                data_reading = ""
            elif (data_reading == "~ CAMERAS ~") :
                cameras = int(line)
                data_reading = ""
            elif (data_reading == "~ GUARDS ~") :
                guards = int(line)
                data_reading = ""
            elif (data_reading == "~ MANAGER ~") :
                manager_locked = bool(line)
                data_reading = ""
            elif (data_reading == "~ JANITOR ~") :
                janitor_locked = bool(line)
                data_reading = ""
            elif (data_reading == "~ SECURITY ~") :
                security_locked = bool(line)
                data_reading = ""
                #print("current  room changed")
    print("Loaded Succesfully.")



def create_save():
    #This function saves all the important game details to a text file.
    #Data is formatted appropriately, so that it can be read correctly during the load function.
    #This is done by using special character such as '#' that can be detected and removed later on.
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
        new_save.write(str(guards) + "\n")
        new_save.write("~ MANAGER ~" + "\n")
        new_save.write(str(manager_locked) + "\n")
        new_save.write("~ JANITOR ~" + "\n")
        new_save.write(str(janitor_locked) + "\n")
        new_save.write("~ SECURITY ~" + "\n")
        new_save.write(str(security_locked))
        print("Saved Succesfully.")
    #new_save.close()




if __name__ == "__main__":
    main()

