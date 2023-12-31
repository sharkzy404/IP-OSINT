import requests
import json as js
import time as tm
import sys
from colorama import Fore as Fr, Style as St
import socket
from os import system as syst

syst("clear")

def banner():
    data = """
                           Mr.SHARK IP OSINT
                •♪••••••••Powered by ipinfo.io••••••♪••••
    """
    print(Fr.YELLOW+data)
    St.RESET_ALL

def get_ip_details():
    print (Fr.BLUE+"[*]To Get device ip info :Y: \n[*]To get quest ip info :N:\n[*]••To clear screen :clear:")
    print (" ")
    inp = input(Fr.YELLOW+"[*]: "+St.RESET_ALL).upper()
    print (" ")
    if inp == "Y":
        print (Fr.GREEN+"[*]Loading")
        tm.sleep(2)
        num = 0
        while True:
            num += 1
            try:
                url = requests.get("https://ipinfo.io")
                break
            except:
                print (Fr.RED+"[x]No internet connection", num)
                tm.sleep(0.5)
                pass
    elif inp == "N":
        while True:
            try:
                ip = input(Fr.GREEN+"[*]Guest IP: "+St.RESET_ALL)
                print (" ")
                break
            except:
                print (Fr.RED+"[x]Bad inputs")
                pass
        print (Fr.YELLOW+"[*]Loading\n")
        tm.sleep(2)
        num = 0
        while True:
            num += 1
            try:
                url = requests.post("https://ipinfo.io", json={"ip":ip})
                break
            except:
                print (Fr.RED+"[x]No internet connection", num)

                tm.sleep(0.5)
                try:
                    if socket.gethostbyname("facebook.com") == True:
                        break
                except socket.gaierror:
                    pass
    elif inp == "CLEAR":
        syst('clear')
        run_engine()

    else:
        print (Fr.RED+"[x]Invalid")
        quit(0)

    data = url.text
    res = url.status_code

    if res == 200:
        load = js.loads(data)
        keys = load.keys()

        for key in keys:
            key_info = key
            data_info = load[key_info]
            print (Fr.YELLOW+"[✓] "+key+": "+Fr.GREEN+str(data_info))
        print (" ")
        tm.sleep(3)

    elif res == 404:
        print (Fr.RED+"[x]Error, invalid ip address")
        print (" ")
        tm.sleep(3)





def run_engine():
    banner()
    while True:
       get_ip_details()

run_engine()
