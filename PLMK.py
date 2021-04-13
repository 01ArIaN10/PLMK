from colorama import Fore
from modules import Intro , Banner , Exit
from datetime import datetime
def RM_NULL(LIST):
    N_LIST=[]
    for i in LIST:
        if i!="" and i!=None:
            N_LIST+=[i]
    return N_LIST

Intro.SHOW()
Banner.SHOW()

while True:
    inputs=input(Fore.RED+"┌─["+Fore.LIGHTGREEN_EX+"Your Inputs"+Fore.RED+"("+Fore.WHITE+"Split Them By"+Fore.YELLOW+" ; "+Fore.RED+")" """]
└──╼ """+Fore.WHITE+"» "+Fore.RESET)
    word=inputs.split(";")
    word=RM_NULL(word)
    if len(word)<2:
        print(Fore.RED+"Invalid Input!"+Fore.RESET)
    else:
        break

while True:
    mix_num=input(Fore.RED+"┌─["+Fore.LIGHTGREEN_EX+"How Many Word Do You Want To Mix"+Fore.RED+"("+Fore.WHITE+"Default = "+Fore.YELLOW+str(len(word))+Fore.RED+")" """]
└──╼ """+Fore.WHITE+"» "+Fore.RESET)
    if mix_num=="":
        mix_num=len(word)
    if not 1<=int(mix_num)<=len(word):
        print(Fore.RED+"Invalid Input!"+Fore.RESET)
    else:
        break

out_num=0
for num in range(int(mix_num)):
    out_num+=len(word)**(num+1)
while True:
    OK=input(Fore.RED+"┌─["+Fore.LIGHTGREEN_EX+"You Will Have "+str(out_num)+" Passwords , Do You Want Continue"+Fore.RED+"("+Fore.WHITE+"Y"+Fore.RED+"/"+Fore.WHITE+"n"+Fore.RED+")" """]
└──╼ """+Fore.WHITE+"» "+Fore.RESET)
    if OK.lower()=="y" or OK.lower()=="yes" or OK.lower()=="n" or OK.lower()=="no" or OK=="" :
        if OK.lower()=="y" or OK.lower()=="yes" or OK=="":
            OK=True
            break
        else:
            OK=False
            Exit.EX()
    else:
        print(Fore.RED+"Invalid Input!"+Fore.RESET)

if OK==True:
    print()
    start=datetime.now()
    build="import sys\n"
    build+="words="+str(word)+"\n"
    build+="file=open('Passwords.txt','w')\n"
    build+="_out_num="+str(out_num)+"\n"
    build+="prog_num=1\n"
    build+="percent=0\n"
    build+="sys.stdout.write(Fore.WHITE+'Progress'+Fore.YELLOW+' => '+Fore.RED+'{'+50*' '+'}'+Fore.YELLOW+' 0 %')\n"
    build+="sys.stdout.flush()\n"
    for i in range(int(mix_num)):
        tab=""
        output=""
        for j in range(i+1):
            build+=tab+"for a"+str(j)+" in words:\n"
            tab+="   "
        for k in range(i+1):
            output+="a"+str(k)+"+"
        build+=tab+"file.write("+output[:len(output)-1]+"+chr(10))\n"
        build+=tab+"if int((prog_num*100)/_out_num) != percent:\n"
        build+=tab+"    percent=int((prog_num*100)/_out_num)\n"
        build+=tab+"    progress=Fore.WHITE+'Progress'+Fore.YELLOW+' => '+Fore.RED+'{'+Fore.GREEN+(int(percent/2)*'#')+((50-(int(percent/2)))*' ')+Fore.RED+'}'+Fore.YELLOW+' '+str(percent)+' %'\n"
        build+=tab+"    sys.stdout.write(chr(8)*len(progress))\n"
        build+=tab+"    sys.stdout.write(progress)\n"
        build+=tab+"    sys.stdout.flush()\n"
        build+=tab+"prog_num+=1\n"
    build+="file.close()"
    exec(build)
    end=datetime.now()
    print("\n\n"+Fore.LIGHTGREEN_EX+str(out_num)+f" Passwords Saved In Passwords.txt \n Time={end-start}"+Fore.RESET)
    Exit.EX()

