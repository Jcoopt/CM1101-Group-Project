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
            print(item)
            # print(str(i) + ") " + item["action"] + " " + item["id"].upper() + " to " + item["action"].lower() + " " + item["name"] + "." + " (" + "£" + str(item["value"]) + ", " + str(item["mass"]) + "kg)")
            # print("{0}){1} {2} to {3} {4}. (£{5}, {6}kg".format(i,item["action"],item["id"].upper(),item["action"].lower(),item["name"],item["value"],item["mass"]))
            i += 1

        print(str(i) + ") " + "LEAVE to leave the shop and back to home.")
    else:
        for item in location["items"]:
            print(str(i) + ") " + item["action"] + " " + item["id"].upper() + " to " + item["action"].lower() + " " +
                  item["name"] + "." + " (Free, " + str(item["mass"]) + "kg)")
            i += 1

        print(str(i) + ") " + "SLEEP to sleep and go to the next day.")


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
        else:
            print("Buy what?\n")

    elif command[0] == "take":
        if len(command) > 1:
            pre_game_excute_take(command[1])
        else:
            print("Take what?\n")

    elif command[0] == "drink":
        if len(command) > 1:
            pre_game_excute_drink(command[1])
        else:
            print("Drink what?\n")

    elif command[0] == "leave" and pre_game_location == location_bar:
        print("You left the shop and go to the shop.\n")
        pre_game_location = location_shop
        return False

    elif command[0] == "leave" and pre_game_location == location_shop:
        print("You left the shop and back to home.\n")
        pre_game_location = location_home
        return False

    elif command[0] == "sleep" and pre_game_location == location_home:
        print("You sleep!\n")
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

    while True:
        pre_game_print_option(location_shop)
        user_input = pre_game_excute(pre_game_read_user_input())

        if user_input is False:
            break


def pre_game_home():
    # print("") <-- print the story

    while True:
        pre_game_print_option(location_home)
        user_input = pre_game_excute(pre_game_read_user_input())

        if user_input is False:
            break

# --------- main pre-game part --------- #


