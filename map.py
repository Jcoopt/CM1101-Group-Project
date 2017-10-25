import items
from items import *

#Incomplete!
location_entry_exit1 = {
    "name": "Main Entrance",

    "description":
    """The entrance to the bank. Several security cameras overhang the steel impact-resistant doors.
    Three unarmed security guards are patrolling the entrance.""",

    "exits": {"east": "Consultation Room"}, 

    "contents": {"Security Cameras"},

    "option1": {""}
  
}

location_entry_exit2 = {
    "name": "Secondary Entrance",

    "description":
    """The alternative entrance to the bank. Several security cameras overhang the steel impact-resistant doors.
    No security guards are in sight, however the areas is fairly crowded with customers.""",

    "exits": {"south": "Lobby"},

    "contents": {"Security Cameras"},

    "option1": {""}
  
}

location_consultation_room = {
    "name": "The Consultation Room",

    "description":
    """Consultation boothes are scattered around the room. It would appear that all employees are pre-occupied with customers,
    a single security camera watches from the south-east corner of the room.""",

    "exits": {"west": "Entrance/Exit", "south": "Manager's Office", "east": "Lobby", "west": "Entry/Exit1"},

    "contents": {"Security Cameras"},

    "option1": {""}
}

location_managers_office = {
    "name": "The Manager's Office",

    "description":
    """The Manager of the bank resides here from 9:00 to 19:00. The manager keeps a close eye on security and is constantly on
    high alert. The Office itself is locked, entry is only permitted by using the intercom and requesting entry from the manager himself.""",

    "exits": {"north": "Consultation Room"} ,

    "contents": {"Keycard", "Credit Card", "Security Cameras"},

    "option1": {""}
}

location_lobby = {
    "name": "The Lobby",

    "description":
    """The lobby of the bank. This area is the least guarded of the bank, employees enter and leave frequently,
    but only one security guard is to be seen. A mysterious object is located in the plant, south of the room.""",

    "exits": {"east": "Bank Tellers", "south": "Security Office", "west": "Consultation Room", "north": "Entry/Exit2"}, 

    "contents": {"Security Guard"},

    "option1": {""}
}

location_security_office = {
    "name": "The Security Office",

    "description":
    """All activity within the bank is monitered from this station. The office is operated by several security officers,
    all of which are currently watching the live CCTV feedback. They are unaware of your presence. """,

    "exits": {"north": "Lobby"}, 

    "contents": {"Security Cameras"},

    "option1": {""}
}

location_bank_tellers = {
    "name": "Bank Tellers",

    "description":
    """The easternmost location in the bank. The room is filled with mostly employees and customers, it is quite loud in
    the room, you can barely hear yourself think.""",

    "exits": {"west": "Lobby", "south": "Vault"}, 

    "contents": {"Security Cameras", "Bank Tellers"},

    "option1": {""}
}


location_vault = {
    "name": "The Vault",

    "description":
    """All of the banks valuables are stored here. Security cameras are located on each corner of the room.
    The vault itself is made of a special concrete with a steel cladding, reinforced with a network of steel rods. 
    The vault is secured electronically with two key card scanners, as well as a combination lock. You notice that the locks
   are alarmed, and will most likely be set off after a single failed attempt of entry.""",

    "exits": {"south":"Bank Tellers"}, 

    "contents": {"Security Cameras"},

    "option1": {}
}

areas = {
	"Vault": location_vault,
	"Bank Tellers": location_bank_tellers,
	"Security Office": location_security_office,
	"Lobby": location_lobby,
	"Manager's Office": location_managers_office,
	"Consultation Room": location_consultation_room,
	"Entry/Exit1": location_entry_exit1,
	"Entry/Exit2": location_entry_exit2
}



# ------------------------------------------- #
# pre_heist part map (don't add it to arears!)
# ------------------------------------------- #
location_bar = {
    # story description and dialog (incomplete)
    "description": '''Story Part - BAR''',

    "items": [item_drinks]
}


location_shop = {
    # story description and dialog (incomplete)
    "description:": '''Story Part - SHOP''',

    "items": [item_sneakers, item_lunch_box, item_screwdriver, item_wire_cutter]
}


location_home = {
    # story description and dialog (incomplete)
    "description:": '''Sory Part - HOME''',

    "items": [item_ski_mask, item_backpack, item_laptop, item_vodka, item_donats]
}