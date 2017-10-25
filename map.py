import items
from banner import *

location_entry_exit = {
    "name": "Entrance/Exit",

    "description":
    """The entrance to the bank. Several security cameras overhang the steel impact-resistant doors.
    One unarmed security guards are patrolling the entrance.""",

    "exits": {"east": "Consultation Room"},

    "contents": ["paperclip","securitycamera", "securityguard"],

    "banner": exit_banner
}


location_consultation = {
    "name": "Consultation Room",

    "description":
    """Consultation boothes are scattered around the room. It would appear that all employees are pre-occupied with customers,
    a single security camera watches from the south-east corner of the room.""",

    "exits": {"west": "Entrance/Exit", "south": "Manager's Office", "east": "Lobby", "north": "Janitors"},

    "contents": ["securitycamera", "securityguard", "screwdriver"],

    "banner": consultation_banner
}


location_managers = {
    "name": "Manager's Office",

    "description":
    """The Manager of the bank resides here from 9:00 to 19:00. The manager keeps a close eye on security and is constantly on
    high alert. The Office itself is locked, entry is only permitted by using the intercom and requesting entry from the manager himself.""",

    "exits": {"north": "Consultation Room"},

    "contents": ["keycard", "securitycamera"],

    "banner": manage_banner
}


location_lobby = {
    "name": "Lobby",

    "description":
    """The lobby of the bank. This area is the least guarded of the bank, employees enter and leave frequently,
    but only one security guard is to be seen. A mysterious object is located in the plant, south of the room.""",

    "exits": {"east": "Bank Tellers", "south": "Security Office", "west": "Consultation Room", "north": "Toilets"}, 

    "contents": ["securityguard", "energydrink"],

    "banner": lobby_banner
}


location_security = {
    "name": "Security Office",

    "description":
    """All activity within the bank is monitered from this station. The office is operated by several security officers,
    all of which are currently watching the live CCTV feedback. They are unaware of your presence. """,

    "exits": {"north": "Lobby"}, 

    "contents": ["securitycamera", "controlpanel", "securityguard"],

    "banner": security_banner
}


location_tellers = {
    "name": "Bank Tellers",

    "description":
    """The easternmost location in the bank. The room is filled with mostly employees and customers, it is quite loud in
    the room, you can barely hear yourself think.""",

    "exits": {"west": "Lobby", "south": "Vault"}, 

    "contents": ["securitycamera", "banktellers", "securityguard", "note"],

    "banner": bank_banner
}


location_vault = {
    "name": "Vault",

    "description":
    """All of the banks valuables are stored here. Security cameras are located on each corner of the room.
    The vault itself is made of a special concrete with a steel cladding, reinforced with a network of steel rods. 
    The vault is secured electronically with two key card scanners, as well as a combination lock. You notice that the locks
   are alarmed, and will most likely be set off after a single failed attempt of entry.""",

    "exits": {"south":"Bank Tellers"}, 

    "contents": ["securitycamera", "vaultdoor", "securityguard"],

    "banner": vault_banner
}


location_janitor = {
    "name": "Janitors",

    "description":
    """Utilities and other tools are stored here!.""",


    "exits": {"south": "Consultation Room"},

    "contents": ["wirecutters", "vent"],

    "banner": janitors_banner
}


location_Toilet = {
    "name": "Toilets",

    "description":
    """Unisex tolients""",

    "exits":{"south": "Lobby"},

    "contents": ["keys", "toiletpaper"],

    "banner": toilets_banner
}


locations = {
	"Vault": location_vault,
	"Bank Tellers": location_tellers,
	"Security Office": location_security,
	"Lobby": location_lobby,
	"Manager's Office": location_managers,
	"Consultation Room": location_consultation,
	"Entrance/Exit": location_entry_exit,
    "Janitors": location_janitor,
    "Toilets": location_Toilet
}