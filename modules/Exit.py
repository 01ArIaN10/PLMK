from colorama import Fore
import os , platform ,time

def EX():
    _platform=platform.uname()[0]
    if _platform=="Windows":
        clear="cls"
    else:
        clear="clear"
    print()
    print(Fore.LIGHTCYAN_EX+"Thanks For Using!"+Fore.RESET)
    time.sleep(5)
    os.system(clear)
    exit()