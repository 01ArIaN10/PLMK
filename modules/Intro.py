from colorama import Fore
import os , platform , time
def SHOW():
    _platform=platform.uname()[0]
    if _platform=="Windows":
        clear="cls"
    else:
        clear="clear"
    os.system(clear)

    intro_msg=Fore.RED+"Hello My Friend:)"+Fore.RESET
    for i in intro_msg:
        print(i,end="",flush=True)
        time.sleep(0.1)

    os.system(clear)

    print(Fore.GREEN+"""
        
    ▄▄▄       ██▀███   ██▓ ▄▄▄       ███▄    █ 
    ▒████▄    ▓██ ▒ ██▒▓██▒▒████▄     ██ ▀█   █ 
    ▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒▒██  ▀█▄  ▓██  ▀█ ██▒
    ░██▄▄▄▄██ ▒██▀▀█▄  ░██░░██▄▄▄▄██ ▓██▒  ▐▌██▒
    ▓█   ▓██▒░██▓ ▒██▒░██░ ▓█   ▓██▒▒██░   ▓██░
    ▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓   ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
    ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░  ▒   ▒▒ ░░ ░░   ░ ▒░
    ░   ▒     ░░   ░  ▒ ░  ░   ▒      ░   ░ ░ 
        ░  ░   ░      ░        ░  ░         ░
        """+Fore.RESET)
    time.sleep(0.8)
    os.system(clear)

