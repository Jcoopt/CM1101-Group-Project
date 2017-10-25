import items
import map
from map import *

inventory = ["wirecutters", "lunchcoupon", "laptop"] #just to test cutting action, will be picked up during pregame

# player default budget
balance = 100

# player current mass
mass = 0

# max mass
max_mass = 5

current_room = "PLACEHOLDER"

pre_game_location = location_shop


# --------- game status --------- #
manage_status = True
security_status = True
camera_status = True
# --------- game status --------- #

current_room = "Lobby"
current_carry_mass = 0
suspicion = 0
cameras = 6
guards = 6
