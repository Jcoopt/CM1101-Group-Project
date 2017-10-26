# Opening banner for our game
def game_banner():
	print('''
                                                                                                                              
                                                                                                                              
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
                                                                                                                              
                                                                                                                              
                                                                                                                              
 ██████╗  ██████╗███████╗ █████╗ ███╗   ██╗███████╗              ███████╗██╗███████╗████████╗███████╗███████╗███╗   ██╗       
██╔═══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝              ██╔════╝██║██╔════╝╚══██╔══╝██╔════╝██╔════╝████╗  ██║       
██║   ██║██║     █████╗  ███████║██╔██╗ ██║███████╗    █████╗    █████╗  ██║█████╗     ██║   █████╗  █████╗  ██╔██╗ ██║       
██║   ██║██║     ██╔══╝  ██╔══██║██║╚██╗██║╚════██║    ╚════╝    ██╔══╝  ██║██╔══╝     ██║   ██╔══╝  ██╔══╝  ██║╚██╗██║       
╚██████╔╝╚██████╗███████╗██║  ██║██║ ╚████║███████║              ██║     ██║██║        ██║   ███████╗███████╗██║ ╚████║       
 ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝              ╚═╝     ╚═╝╚═╝        ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═══╝       
                                                                                                                              
                                                                                                                              
                                                                                                                              
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
                                                                                                                              
                                                                                                                              
                                                                                                                              
''')


# Ending banner for our game
def end_game_banner():
	print('''
  /$$$$$$                                                     /$$               /$$             /$$     /$$                              
 /$$__  $$                                                   | $$              | $$            | $$    |__/                              
| $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$   /$$   /$$| $$  /$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$$
| $$       /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$|_  $$_/  | $$  | $$| $$ |____  $$|_  $$_/  | $$ /$$__  $$| $$__  $$ /$$_____/
| $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/ /$$$$$$$  | $$    | $$  | $$| $$  /$$$$$$$  | $$    | $$| $$  \ $$| $$  \ $$|  $$$$$$ 
| $$    $$| $$  | $$| $$  | $$| $$  | $$| $$      /$$__  $$  | $$ /$$| $$  | $$| $$ /$$__  $$  | $$ /$$| $$| $$  | $$| $$  | $$ \____  $$
|  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$/| $$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$ /$$$$$$$/
 \______/  \______/ |__/  |__/ \____  $$|__/      \_______/   \___/   \______/ |__/ \_______/   \___/  |__/ \______/ |__/  |__/|_______/ 
                               /$$  \ $$                                                                                                 
                              |  $$$$$$/                                                                                                 
                               \______/                                                                                                  

 /$$     /$$                        /$$      /$$ /$$                 /$$$$$$$$ /$$                        /$$$$$$                                          /$$ /$$ /$$
|  $$   /$$/                       | $$  /$ | $$|__/                |__  $$__/| $$                       /$$__  $$                                        | $$| $$| $$
 \  $$ /$$//$$$$$$  /$$   /$$      | $$ /$$$| $$ /$$ /$$$$$$$          | $$   | $$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$| $$| $$
  \  $$$$//$$__  $$| $$  | $$      | $$/$$ $$ $$| $$| $$__  $$         | $$   | $$__  $$ /$$__  $$      | $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$| $$| $$
   \  $$/| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$| $$  \ $$         | $$   | $$  \ $$| $$$$$$$$      | $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      |__/|__/|__/
    | $$ | $$  | $$| $$  | $$      | $$$/ \  $$$| $$| $$  | $$         | $$   | $$  | $$| $$_____/      | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/                  
    | $$ |  $$$$$$/|  $$$$$$/      | $$/   \  $$| $$| $$  | $$         | $$   | $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$       /$$ /$$ /$$
    |__/  \______/  \______/       |__/     \__/|__/|__/  |__/         |__/   |__/  |__/ \_______/       \______/  \_______/|__/ |__/ |__/ \_______/      |__/|__/|__/
                                                                                                                                                                      
                                                                                                                                                                      
                                                                                                                                                                      
''')


# Banner for display your current location
def shop_banner():
  print('''
──────────────
 ╔═╗╦ ╦╔═╗╔═╗
 ╚═╗╠═╣║ ║╠═╝
 ╚═╝╩ ╩╚═╝╩  
──────────────
''')


# Banner for display your current location
def bar_banner():
	print('''
───────────
 ╔╗ ╔═╗╦═╗
 ╠╩╗╠═╣╠╦╝
 ╚═╝╩ ╩╩╚═
───────────
''')


# Banner for display your current location
def exit_banner():
	print('''
─────────────
 ╔═╗═╗ ╦╦╔╦╗
 ║╣ ╔╩╦╝║ ║ 
 ╚═╝╩ ╚═╩ ╩ 
─────────────
''')


# Banner for display your current location	
def consultation_banner():
	print('''
─────────────────────────────────────────────────
 ╔═╗╔═╗╔╗╔╔═╗╦ ╦╦ ╔╦╗╔═╗╔╦╗╦╔═╗╔╗╔  ╦═╗╔═╗╔═╗╔╦╗
 ║  ║ ║║║║╚═╗║ ║║  ║ ╠═╣ ║ ║║ ║║║║  ╠╦╝║ ║║ ║║║║
 ╚═╝╚═╝╝╚╝╚═╝╚═╝╩═╝╩ ╩ ╩ ╩ ╩╚═╝╝╚╝  ╩╚═╚═╝╚═╝╩ ╩
─────────────────────────────────────────────────
''')


# Banner for display your current location	
def manage_banner():
	print('''
─────────────────────────────────────────
 ╔╦╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔═╗  ╔═╗╔═╗╔═╗╦╔═╗╔═╗
 ║║║╠═╣║║║╠═╣║ ╦║╣ ╚═╗  ║ ║╠╣ ╠╣ ║║  ║╣ 
 ╩ ╩╩ ╩╝╚╝╩ ╩╚═╝╚═╝╚═╝  ╚═╝╚  ╚  ╩╚═╝╚═╝
─────────────────────────────────────────
''')


# Banner for display your current location	
def lobby_banner():
	print('''
─────────────────
 ╦  ╔═╗╔╗ ╔╗ ╦ ╦
 ║  ║ ║╠╩╗╠╩╗╚╦╝
 ╩═╝╚═╝╚═╝╚═╝ ╩ 
─────────────────
''')


# Banner for display your current location	
def security_banner():
	print('''
──────────────────────────────────────────
 ╔═╗╔═╗╔═╗╦ ╦╦═╗╦╔╦╗╦ ╦  ╔═╗╔═╗╔═╗╦╔═╗╔═╗
 ╚═╗║╣ ║  ║ ║╠╦╝║ ║ ╚╦╝  ║ ║╠╣ ╠╣ ║║  ║╣ 
 ╚═╝╚═╝╚═╝╚═╝╩╚═╩ ╩  ╩   ╚═╝╚  ╚  ╩╚═╝╚═╝
──────────────────────────────────────────
''')


# Banner for display your current location	
def bank_banner():
	print('''
─────────────────────────────────────
 ╔╗ ╔═╗╔╗╔╦╔═  ╔╦╗╔═╗╦  ╦  ╔═╗╦═╗╔═╗
 ╠╩╗╠═╣║║║╠╩╗   ║ ║╣ ║  ║  ║╣ ╠╦╝╚═╗
 ╚═╝╩ ╩╝╚╝╩ ╩   ╩ ╚═╝╩═╝╩═╝╚═╝╩╚═╚═╝
─────────────────────────────────────
''')


# Banner for display your current location	
def vault_banner():
	print('''
─────────────────
 ╦  ╦╔═╗╦ ╦╦ ╔╦╗
 ╚╗╔╝╠═╣║ ║║  ║ 
  ╚╝ ╩ ╩╚═╝╩═╝╩ 
─────────────────
''')


# Banner for display your current location	
def janitors_banner():
	print('''
───────────────────────
  ╦╔═╗╔╗╔╦╔╦╗╔═╗╦═╗╔═╗
  ║╠═╣║║║║ ║ ║ ║╠╦╝╚═╗
 ╚╝╩ ╩╝╚╝╩ ╩ ╚═╝╩╚═╚═╝
───────────────────────
''')


# Banner for display your current location
def toilets_banner():
	print('''
─────────────────────
 ╔╦╗╔═╗╦╦  ╔═╗╔╦╗╔═╗
  ║ ║ ║║║  ║╣  ║ ╚═╗
  ╩ ╚═╝╩╩═╝╚═╝ ╩ ╚═╝
─────────────────────
''')