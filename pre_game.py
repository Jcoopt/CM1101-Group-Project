from pre_game_map import *

def print_option(location):
	# print_option(location_bar)
	# print_option(location_shop)
	# print_option(location_home)
	for i in range(len(location["question"])):
		print(str(i + 1) + ") " + location["question"][i])
	

def main_bar():
	# pass	
	print("What are you gonna do?")
	print_option(location_bar)
	print()

	print("Please input your answer as a number.")
	user_iput = input("> ")
	
	if user_iput == 1:
		pass # Manage -> False
	elif user_iput == 2:
		pass # Budget = 99999
	elif user_iput == 3:
		


def main_shop():
	pass


def main_home():
	pass


main_bar()
main_shop()
'''
def pre_bar():
	print(bar["description"] + "\n")
	print("What you gonna do?")

	for i in range(len(bar))


def pre_shop():
	pass


def pre_home():
	pass



bar_list = ["Buy drink for manager.",
			"Steal manager's card.",
			"Quit and go to the shop."]

bar_ans = 0

while True:
	for i in range(len(bar_list)):
		print(str(i + 1) + ". " + bar_list[i])

	print("What do you wanna do?")
	bar_ans = int(input(">")) - 1

	bar_list.remove(bar_list[bar_ans])

	print(bar_list)
'''