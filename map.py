import items
location_entry_exit = {
    "name": "Entrance/exit",

    "description":
    """The entrance to the bank. Several security cameras overhang the steel impact-resistant doors.
    Three unarmed security guards are patrolling the entrance.""",

    "exits": {"east": "Consultation Room", "Security Cameras"}, 

    "contents": {"paperclip"}, 


}



location_consultation = {
    "name": "The Consultation Room",

    "description":
    """Consultation boothes are scattered around the room. It would appear that all employees are pre-occupied with customers,
    a single security camera watches from the south-east corner of the room.""",

    "exits": {"west": "Entrance/Exit", "south": "Manager's Office", "east": "Lobby", "north": "Janitors"},

    "contents": {"Security Cameras", "security guard", "fire alarm"},



}



location_managers = {
    "name": "The Manager's Office",

    "description":
    """The Manager of the bank resides here from 9:00 to 19:00. The manager keeps a close eye on security and is constantly on
    high alert. The Office itself is locked, entry is only permitted by using the intercom and requesting entry from the manager himself.""",

    "exits": {"north": "Consultation Room"},

    "contents": {"Keycard", "Security Cameras", "mini safe", "combination"},


    #The safe contains a note with digits for the vault

    #keycard opens the security room




}




location_lobby = {
    "name": "The Lobby",

    "description":
    """The lobby of the bank. This area is the least guarded of the bank, employees enter and leave frequently,
    but only one security guard is to be seen. A mysterious object is located in the plant, south of the room.""",

    "exits": {"east": "Bank Tellers", "south": "Security Office", "west": "Consultation Room", "north": "Toilets"}, 

    "contents": {"Security Guard", "energy drink"},




}





location_security = {
    "name": "The Security Office",

    "description":
    """All activity within the bank is monitered from this station. The office is operated by several security officers,
    all of which are currently watching the live CCTV feedback. They are unaware of your presence. """,

    "exits": {"north": "Lobby"}, 

    "contents": {"Security Cameras", "note"},



    #The note has the pin for the mini safe in the mangers office.

    #Here the cameras can be turned off using the wire cutters/laptop



}




location_tellers = {
    "name": "Bank Tellers",

    "description":
    """The easternmost location in the bank. The room is filled with mostly employees and customers, it is quite loud in
    the room, you can barely hear yourself think.""",

    "exits": {"west": "Lobby", "south": "Vault"}, 

    "contents": {"Security Cameras", "Bank Tellers", "Security Guard"},





}





location_vault = {
    "name": "The Vault",

    "description":
    """All of the banks valuables are stored here. Security cameras are located on each corner of the room.
    The vault itself is made of a special concrete with a steel cladding, reinforced with a network of steel rods. 
    The vault is secured electronically with two key card scanners, as well as a combination lock. You notice that the locks
   are alarmed, and will most likely be set off after a single failed attempt of entry.""",

    "exits": {"south":"Bank Tellers"}, 

    "contents": {"Security Cameras", "GOLD"},




    #Gold is found here, depending on how many moves you have left is how much gold you can take.




}





location_janitor = {
    "name": "Janitors",

    "description":
    """Utilities and other tools are stored here!.""",


    "exits": {"south": "Consultation"}

    "contents": {"wire cutters", "broom", "paper", "Janitors uniform", "Vent"}

    #To get into the Janitors room you need a picklock or the keys


    #Vent has a secreate passage to the vault, need screw driver or some other peice of equiment to open



}


location_Toilet = {
    "name": "Toilets",

    "description":
    """Unisex tolients"""


    "exits": {"south": "Lobby"}

    "contents": {"keys", "toilet paper"}


    #You noitce dropped keys that are used to open the jantors room
        





}






Locations = {
	"Vault": location_vault,
	"Tellers": location_tellers,
	"Security Office": location_security,
	"Lobby": location_lobby,
	"Manager's Office": location_managers,
	"Consultation Room": location_consultation,
	"Entrance/exit": location_entry_exit,
    "Janitors": location_janitor
    "Toilet": location_Toilet
}