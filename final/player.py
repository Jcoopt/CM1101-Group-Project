import items
import map
from map import *

inventory = [] #just to test cutting action, will be picked up during pregame



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
