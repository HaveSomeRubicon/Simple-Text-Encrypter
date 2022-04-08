import time
import encrypter
import json_utils
import cipher_utils
import os

clear = os.system("clear")


def enter_menu():
    sprint("Press <enter> to continue: ", end)
    input("")


def sprint(text, speed=0.06, wait=0, ending='\n'):
    for each_char in text:
        print(each_char, flush=True, end='')
        time.sleep(speed)
    time.sleep(wait)
    print('', end=ending)


def menu():
    clear
    sprint("Welcome to Text Encrypter V3")
    enter_menu()
    
menu()