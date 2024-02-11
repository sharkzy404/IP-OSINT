import requests
import json as js
import time as tm
import sys
from colorama import Fore as Fr, Style as St
import socket
from os import system as syst

syst("clear")

def banner():
    data = f"""
                        {Fr.CYAN}Mr.SHARK IP OSINT
            {Fr.GREEN}•♪••••••••Powered by ipinfo.io••••••♪••••
    """
    print(data)
    St.RESET_ALL

def device_info():
    print (Fr.GREEN+"[*]Loading\n")
    tm.sleep(0.8)

    try:
        url = requests.get("https://ipinfo.io", timeout=5) 
        data = url.text
        res = url.status_code
        if res == 200:
            load = js.loads(data)
            keys = load.keys()

            for key in keys:
                 key_info = key
                 data_info = load[key_info]
                 print (Fr.CYAN+"[✓] "+key+": "+Fr.BLUE+str(data_info))
            print("\n")

        elif res == 404:
            print(Fr.RED+"[x]Error 404\n")
            
    except requests.Timeout:
        print(Fr.RED+"[x]Error connecting to server\n")

    except requests.exceptions.ConnectionError:
        print(Fr.RED+"[x]No internet connection \n")



def guest_info():
    ip = input(Fr.YELLOW+"[%]Guest ip: "+Fr.WHITE)
    print (Fr.GREEN+"[*]Loading\n")
    tm.sleep(0.8)

    try:
        url = requests.post("https://ipinfo.io", json={"ip":ip}, timeout=5)
        data = url.text
        res = url.status_code
        if res == 200:
            load = js.loads(data)
            keys = load.keys()

            for key in keys:
                key_info = key
                data_info = load[key_info]
                print (Fr.CYAN+"[✓] "+key+": "+Fr.BLUE+str(data_info))
            print("\n")

        elif res == 404:
            print(Fr.RED+"[x]Error 404: invalid IP\n")
    
    except requests.Timeout:
        print(Fr.RED+"[x)Error connecting to server\n")

    except requests.exceptions.ConnectionError:
        print(Fr.RED+"[x]No internet connection\n")



banner()
while True:
    try:
        print(Fr.CYAN+"[*]To get device ip info input < X >\n[*]To get guest ip info input < Y >\n[*]To clear screen < C >")
        inp = input(Fr.YELLOW+"[%]: "+Fr.WHITE).upper()
        if inp == "X":
            device_info()
        elif inp == "Y":
            guest_info()
        elif inp == "C":
            syst("clear")
            banner()
        else:
            print(Fr.RED+"[x]Invalid input\n")
    except KeyboardInterrupt:
        quit(0)



