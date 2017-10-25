<<<<<<< HEAD
item_keycard = {
	"id": "keycard",

	"name": "a keycard to the security office",

	"description": "The magic key that can get you into the security office!",

	"mass": 0.4
}

item_managers_credit_card = {
	"id": "managers_credit_card",

	"name": "manager's Amex credit card",

	"description": "The manager's shiny golden contactless AND limitless Amex card!",

	"mass": 0.5
}

item_lunch_coupon = {
    "id": "lunch_coupon",

    "name": "free meal deal coupon",
    
    "description": "Coupon for a free meal deal at The Corner Shop (which are so bad they should be free anyway).",

    "mass": 0.1
}

item_combination = {
	 "id": "combination",

    "name": "the combination to the vault",
    
    "description": "The only thing that stands between you and the diamonds.",
    
    "mass": 0.1
}


# List of items you can buy or take in the bar
item_drinks = {
	"id": "drinks",

	"name": "some drinks",

	"description": " ",

	"mass": 0.1,

	# the price of this itme
	"value": 50
}



# List of items you can buy in the shop
item_sneakers = {
	"id": "sneakers",

	"name": "a pair of sneaker",

	"description": " ",

	"mass": 1,

	# the price of this itme
	"value": 50,

	"action": "BUY"
}

item_lunch_box = {
	"id": "lunch",

	"name": "a set of lunch",

	"description": " ",

	"mass": 3,

	# the price of this itme
	"value": 50,

	"action": "BUY"
}

item_screwdriver = {
	"id": "screwdriver",

	"name": "a screwdriver",

	"description": " ",

	"mass": 2,

	# the price of this itme
	"value": 50,

	"action": "BUY"
}

item_wire_cutter = {
	"id": "cutter",

	"name": "a wire cutter",

	"description": " ",

	"mass": 4,

	# the price of this itme
	"value": 50,

	"action": "BUY"
}

# List of items you can find in your home
item_ski_mask = {
	"id": "mask",

	"name": "a ski mask",

	"description": " ",

	"mass": 0.1,

	# the price of this itme
	"value": 0,

	"action": "TAKE"
}

item_backpack = {
	"id": "backpack",

	"name": "a large backpack",

	"description": " ",

	"mass": 0,

	# the price of this itme
	"value": 0,

	"action": "TAKE"
}

item_laptop = {
	"id": "laptop",

	"name": "a laptop",

	"description": " ",

	"mass": 0.1,

	# the price of this itme
	"value": 0,

	"action": "TAKE"
}

item_vodka = {
	"id": "vodka",

	"name": "a bottle of vodka",

	"description": " ",

	"mass": 0.1,

	# the price of this itme
	"value": 0,

	"action": "DRINK"
}

item_donats = {
	"id": "donats",

	"name": "some donats",

	"description": " ",

	"mass": 0.1,

	# the price of this itme
	"value": 0,

	"action": "TAKE"
=======
#note: keep IDs lowercasee

item_keycard = {
	"id": "keycard",

	"name": "A keycard [Security office]",

	"description": "The magic key that can get you into the security office!",

	"mass": 0.4,

	"action": ["Take"],

	"undo_action": "Drop"
}

item_managers_credit_card = {
	"id": "managers_credit_card",

	"name": "Manager's Amex credit card",

	"description": "The manager's shiny golden contactless AND limitless Amex card!",

	"mass": 0.5,

	"action": ["Steal"],

	"undo_action": "Drop"
}

item_lunch_coupon = {
    "id": "lunchcoupon",

    "name": "Free meal deal coupon",
    
    "description": "Coupon for a free meal deal at The Corner Shop (which are so bad they should be free anyway).",

    "mass": 0.1,

    "action": ["Take"],

    "undo_action": "Drop"
}

item_combination = {
	 "id": "combination",

    "name": "The combination to the vault",
    
    "description": "The only thing that stands between you and the diamonds.",
    
    "mass": 0.1,

    "action": ["Take"],

    "undo_action": "Drop"
}

item_paperclip = {
	 "id": "paperclip",

    "name": "Random paperclip",
    
    "description": "Single paperclip that can be used as a picklock",
    
    "mass": 0.08,

    "action": ["Take"],

    "undo_action": "Drop"
}

item_note = {
	 "id": "note",

    "name": "Post-it note",
    
    "description": "A post-it note that contains the combination to the mini-safe.",
    
    "mass": 0.09,

    "action": ["Take"],

    "undo_action": "Drop"
}

item_gold = {
	 "id": "gold",

    "name": "Gold",
    
    "description": "The treasure.",
    
    "mass": 1,

    "action": ["Steal"],

    "undo_action": "Drop"
}



# List of items you can buy in the shop
item_sneakers = {
	"id": "sneakers",

	"name": "a pair of sneakers",

	"description": "A battered pair of Nike Air Force 1s, the least squeaky shoes in the world.",

	"mass": 0.1,

	"action": ["Wear"],

	"undo_action": "Drop"
}

item_lunch_box = {
	"id": "lunch_box",

	"name": "a Lunch box",

	"description": "Original Power Rangers lunch box in case you get hungry mid-heist.",

	"mass": 0.1,

	"action": ["Take"],

	"undo_action": "Drop"
}

item_screwdriver = {
	"id": "screwdriver",

	"name": "a Screwdriver",

	"description": "Rusty and second hand but reliable",

	"mass": 0.1,

	"action": ["Take"],

	"undo_action": "Drop"
}

item_wire_cutter = {
	"id": "cutter",

	"name": "a wire cutter",

	"description": "Brand new wire cutters that can cut through anything in its path.",

	"mass": 0.1,

	"action": ["Take"],

	"undo_action": "Drop"
}

# List of items you can find in your home
item_ski_mask = {
	"id": "mask",

	"name": "a Ski mask",

	"description": "Plain black ski mask to hide your identity",

	"mass": 0.1,

	"action": ["Wear"],

	"undo_action": "Drop"
}

item_backpack = {
	"id": "backpack",

	"name": "a Large backpack",

	"description": "A backpack with a large capacity to hold all of your 'winnings'.",

	"mass": 0.1,

	"action": ["Take"],

	"undo_action": "Drop"
}

item_laptop = {
	"id": "laptop",

	"name": "a Laptop",

	"description": "The new MacBook Pro with built-in 3G for use literally anywhere!",

	"mass": 0.5,

	"action": ["Take"],

	"undo_action": "Drop"
}

item_vodka = {
	"id": "vodka",

	"name": "a Bottle of vodka",

	"description": "A large 10l bottle of Smirnoff",

	"mass": 0.9,

	"action": ["Drink"],
}

item_donuts = {
	"id": "donuts",

	"name": "some Donuts",

	"description": "An 11 piece box of Crispy Kreme's finest donut selection ",

	"mass": 0.2,

	"action": ["Take"],

	"undo_action": "Drop"
}

item_security_guard = {
    "id": "security",

    "name": "A Security Guard",

    "description": "A slightly pudgy middle aged man with a penchant for Donuts",

    "mass": 0.2,

    "action": ["Punch", "Bribe"],

    "undo_action": "Apologise"
    
}

item_security_camera = {
    "id": "securitycamera",

    "name": "A Security Camera",

    "description": "An oblong box on the ceiling with a lens on one end. if it weren't for the blinking light "
                   "you would wonder if it were even working",

    "mass": 0.2,

    "action": ["Cut"],

    "undo_action": "Drop"

}



item_tellers = {
    "id": "teller",

    "name": "a Teller",

    "description": "a Kiosk with a thick glass covering",

    "mass": 8,

    "action": ["Pick up"],

    "undo_action": "Drop"
}

item_drill = {
	"id": "drill",
	
	"name": "A Drill",
	
	"description": "a heavy drill, great for breaking into vaults",
	
	"mass": 0.8,

	"action": ["Take"],

	"undo_action": "Drop"
}
	
	
	
# more items found in bank
item_energy_drink = {
	"id": "energy_drink",
	
	"name": "Energy drink",
	
	"description": "A large can of Monster",
	
	"mass": 0.3,

	"action": ["Take"],

	"undo_action": "Drop"
}

item_family_picture = {
	"id": "family_picture",
	
	"name": "Family Picture",
	
	"description": "a crumpled up picture, depicting three smiling people",
	
	"mass": 0.1,

	"action": ["Take"],

	"undo_action": "Drop"
}

item_fire_alarm = {
	"id": "fire_alarm",
	
	"name": "Fire Alarm",
	
	"description": "Don't set it off...",
	
	"mass": 0.1,

	"action": ["Steal"],

	"undo_action": "Drop"
}

item_keys = {
	"id": "keys",
	
	"name": "Keys",
	
	"description": "Hmm, I wonder what they unlock.",
	
	"mass": 0.1,

	"action": ["Steal"],

	"undo_action": "Drop"
}


item_toilet_paper = {
	"id": "toilet_paper",

	"name": "Toilet paper",

	"description": "Nice.",

	"mass": 0.4,

	"action": ["Take"],

	"undo_action": "Drop"
}

item_broom = {
	"id": "broom",

	"name": "a Broom",

	"description": "For sweeping only.",

	"mass": 0.1,

	"action": ["Take"],

	"undo_action": "Drop"
}

item_paper = {
	"id": "paper",

	"name": "Paper",

	"description": "Hmmmmmm.",

	"mass": 0.1,

	"action": ["Take"],

	"undo_action": "Drop"
}


item_janitor_uniform = {
	"id": "janitorsuniform",

	"name": "Janitor's uniform",

	"description": "NOT for disguises.",

	"mass": 0.3,

	"action": ["Wear"],

	"undo_action": "Drop"
}

item_vent = {
	"id": "vent",

	"name": "Vent",

	"description": "You could climb through this.",

	"mass": 0.8,

	"action": ["Unscrew"],

	"undo_action": "Re-screw"
}

item_mini_safe= {
	"id": "minisafe",

	"name": "Mini safe",

	"description": "There could be money in this.",

	"mass": 5,

	"action": ["Steal from"],

	"undo_action": "Replace contents"
}

item_control_panel= {
	"id": "controlpanel",

	"name": "Control Panel",

	"description": "Controls all the security camera's in the bank.",

	"mass": 5,

	"action": ["Deactivate all Cameras on"],

	"undo_action": "Reactivate cameras"
}

item_vault_door= {
	"id": "vaultdoor",

	"name": "Vault door",

	"description": "The final boss.",

	"mass": 99,

	"action": ["Use drill on", "Enter combination on"],

	"undo_action": "Close"
}


item_index = {
    "donuts": item_donuts, #done
    "vodka": item_vodka,
    "laptop": item_laptop, #done
    "backpack": item_backpack,
    "mask": item_ski_mask,
    "wirecutters": item_wire_cutter, #done
    "screwdriver": item_screwdriver,
    "lunchbox": item_lunch_box,
    "securityguard": item_security_guard, #done
    "securitycamera": item_security_camera, #done
    "banktellers": item_tellers,
	"energydrink": item_energy_drink,
	"familypicture": item_family_picture,
	"drill": item_drill, #done
	"gold": item_gold, #done
	"lunchcoupon": item_lunch_coupon, #done
	"managerscreditcard": item_managers_credit_card,
	"keycard": item_keycard, #done
	"combination": item_combination, #done
	"sneakers": item_sneakers,
	"skimask": item_ski_mask,
	"paperclip": item_paperclip,
	"firealarm": item_fire_alarm,
	"note": item_note,
	"keys": item_keys,
	"toiletpaper": item_toilet_paper,
	"broom": item_broom,
	"paper": item_paper,
	"janitorsuniform": item_janitor_uniform,
	"vent": item_vent, #done
	"minisafe": item_mini_safe, 
	"controlpanel": item_control_panel, #done
	"vaultdoor":item_vault_door #done
>>>>>>> 5262cfdefdaa33650652b986bb8affeab09fd938
}