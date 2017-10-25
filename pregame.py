from items import *
from gameparser import *
import os
import time
import player
global inventory
inventory= player.inventory

location_bar = {
    # story description and dialog (incomplete)
    "description": '''Story Part - BAR''',

    "items": [item_drinks]
}

location_shop = {
    # story description and dialog (incomplete)
    "description:": '''Story Part - SHOP''',

    "items": [item_sneakers, item_lunch_box, item_screwdriver, item_wire_cutter,item_laptop]
}


location_home = {
    # story description and dialog (incomplete)
    "description:": '''Story Part - HOME''',

    "items": [item_ski_mask, item_backpack, item_laptop, item_vodka, item_donuts],
}

shop_items={

}
def logic_box_balance(balance, value):
    if balance - value >= 0:
        return 0
    else:
        return 1


def logic_box_mass(mass, value):
    if mass + value <= max_mass:
        return 0
    else:
        return 1


# --------- print menu --------- #
def pre_game_print_option(location):
    i = 1
    print("Which of the following action will you take?")

    if location == location_bar:
        # INCOMPLETE
        pass
    elif location == location_shop:
        for item in location["items"]:
            print("{0}) {1} to buy {2}. (£{3})".format(i,item["id"].upper(),item["name"],item["value"]))


        print(str(i) + ") " + "LEAVE to leave the shop and back to home.")



def pre_game_print_balance():
    print("<-- You have £" + str(balance) + " left -->")


def pre_game_print_mass():
    print("<-- Total mass of your inventory is " + str(mass) + " kg" + ". -->\n")


# --------- print menu --------- #


def pre_game_read_user_input():
    user_input = input("> ")
    return normalise_input(user_input)


# --------- game excute part --------- #
def pre_game_excute_buy(item_id):
    global balance
    global mass
    buy_status = False
    if item_index[item_id] in location_shop["items"]:
            inventory.append(item_id)
            location_shop["items"].remove(item_index[item_id])
            print("you have bought {}".format(item_index[item_id]["name"]))

    """
    print(location_shop["items"])
    for i in range(len(pre_game_location["items"])):
        if item_id in pre_game_location["items"][i]["id"] and logic_box_balance(balance, pre_game_location["items"][i][
            "value"]) == 0 and logic_box_mass(mass, pre_game_location["items"][i]["mass"]) == 0:
            balance -= pre_game_location["items"][i]["value"]
            mass += pre_game_location["items"][i]["mass"]
            print("------------------------------------")
            print("You bought " + pre_game_location["items"][i]["name"] + "!")
            print(balance)
            print(mass)
            print("------------------------------------\n")
            inventory.append(pre_game_location["items"][i])
            pre_game_location["items"].remove(pre_game_location["items"][i])
            buy_status = True
            break

    if not buy_status:
        if not buy_status and logic_box_balance(balance, pre_game_location["items"][i]["value"]) == 1:
            print("------------------------------------")
            print("You bought " + pre_game_location["items"][i]["name"] + "!")
            print(balance)
            print(mass)
            print("------------------------------------\n")
            print("You don't have enough money to buy this.")
        elif not buy_status and logic_box_mass(mass, pre_game_location["items"][i]["mass"]) == 1:
            print("------------------------------------")
            print("You bought " + pre_game_location["items"][i]["name"] + "!")
            print(balance)
            print(mass)
            print("------------------------------------\n")
            print("It too heavy!")

        print("You cannot buy this item.\n")
        print(i)
        """
def pre_game_excute_take(item_id):
    global mass
    take_status = False

    for i in range(len(pre_game_location["items"])):
        if item_id in pre_game_location["items"][i]["id"] and logic_box_mass(mass, pre_game_location["items"][i][
            "mass"]) == 0:
            mass += pre_game_location["items"][i]["mass"]
            print("------------------------------------")
            print("You take " + pre_game_location["items"][i]["name"] + "!")
            print(balance)
            print(mass)
            print("------------------------------------\n")
            inventory.append(pre_game_location["items"][i])
            pre_game_location["items"].remove(pre_game_location["items"][i])
            take_status = True
            break

    if not take_status:
        print("You can't take this item.\n")


def pre_game_excute_drink():
    pass


def pre_game_excute(command):
    global pre_game_location

    if 0 == len(command):
        return

    if command[0] == "buy":
        if len(command) > 1:
            pre_game_excute_buy(command[1])
            return True
        else:
            print("Buy what?\n")
            return True

    elif command[0] == "drink":
        if len(command) > 1:
            pre_game_excute_drink(command[1])
        else:
            print("Drink what?\n")

    elif command[0] == "leave":
        print("You leave the shop and go home.\n")
        pre_game_location = location_shop
        return False


    else:
        print("This makes no sense.\n")


# --------- game excute part --------- #


def pre_game_cal_mass(item_mass, total_mass):
    # cal
    return item_mass + total_mass


def pre_game_cal_budget(balance, value):
    # cal_budget(balance, )
    return balance - value


# --------- main pre-game part --------- #
def pre_game_bar():
    # print("") <-- print the story

    pre_game_print_option(location_bar)
    pre_game_read_user_input()


def pre_game_shop():
    # print("") <-- print the story
    user_input=True
    while user_input:
        pre_game_print_option(location_shop)
        user_input = pre_game_excute(pre_game_read_user_input())
    return inventory
# --------- main pre-game part --------- #

def print_ch_by_ch(text,wait):
    os.system('cls')
    full_text=""
    for ch in text:
        full_text="{0}{1}".format(full_text, ch)
        print(full_text)
        time.sleep(wait)
        os.system('cls')

    print(full_text)



def display_start_dialog():
    intro_pt1 = """You are in a rustic bar in the Upper West Side of Manhattan. \n\nIt's a friday night and you'd much rather be at home with Netflix and a bottle of Jack Daniels,
    but your good friend Joe insisted on meeting for a drink to discuss yet another one of the 'big ideas' he so often has.
    \nJoe is a janitor and he usually comes to you with these worthless notions after a long shift, but this time he looks serious.
    \n \nJoe: I've been thinking..."""

    print_ch_by_ch(intro_pt1, 0.01)

    user_name = input("Before we proceed, what is your chosen name?: ")

    intro_pt2 = "Joe: I've been thinking, " + user_name + """\n\nJoe: What makes those rich stockbrokers over there any better than us? \n \n
    You look over and see a group of young entrepeneurs laughing, smoking and drinking whiskey as if they were in the The Wolf of Wall Street
    \nYou: They have too much money, and we don't have enough.
    \nJoe: Exactly! That's where my idea came from. The only difference between us and them is money. And the easiest way to aquire money?
    \nYou: I don't know, theft
    \nJoe: Right again! On thursdays, I clean the lobby and bathrooms in the Gotham National Bank, and the security is so minimal, I think we could do it!
    \nYou: Surely you're not serious?
    \nYou've seen Joe steal a few Cadburys Creme Eggs before, but nothing like this.
    \nJoe: I'm deadly serious. How are we going to make it in this world by cleaning bathrooms all day?
    \nJoe has a point, and you've seen it been pulled off in all of your favourite action movies, so you eventually (after a few shots) agree to go for it.
    \n"Joe: Tomorrow then. \n You: Yeah, tomorrow then."""

    print_ch_by_ch(intro_pt2, 0.01)


