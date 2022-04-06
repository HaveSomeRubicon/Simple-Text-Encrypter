import time
import encrypter
import json_utils
import cipher_utils
import os


def clear(): return os.system("clear")


def option_menu():
    clear()
    print("""OPTION MENU:
          type E to encrypt
          type D to decrypt
          type L to list all your keys
          type E to edit a keys title
          """)


def encrypt_menu():
    clear()
    print("WHAT KEY WOULD YOU LIKE TO USE TO ENCRYPT?")
    ciphers = json_utils.export_json_file()["ciphers"]
    ciphnum = 0
    time.sleep(0.5)
    for each_cipher in ciphers:
        time.sleep(0.2)
        print(
            f"{ciphnum}. Title: {each_cipher['title']}, created on: {each_cipher['date']}")
        ciphnum += 1
    choice = int(
        input(f"\nEnter the number for the key you want to use(0-{ciphnum-1}): "))
    if choice > ciphnum - 1:
        print("Invalid number error: please restart the program")
        quit()
    time.sleep(0.5)

    clear()
    choice2 = input("What text would you like to encrypt?: ")
    time.sleep(0.5)

    clear()
    print("ENCRYPTED TEXT:")
    print(encrypter.encrypt(choice2, ciphers[choice - 1]["cipher"]))
    choice = input("Press <enter> to go back to the menu")
    option_menu()


clear()
print("""
╔═╗░░░░░░╔╗░░░░░░░░░░░╔╗░░╔╗░░░░░░░░░░░░░░░░░░░░░
║╬╠╦╦═╦╦╦╝╠╗╔╦╗╔══╦═╗╔╝╠═╗║╚╦╦╗╔╗░░░░░░░░░░░░░░░░
║╔╣╔╣╬║║║╬║╚╣║║║║║║╬╚╣╬║╩╣║╬║║║╠╣░░░░░░░░░░░░░░░░
╚╝╚╝╚═╩═╩═╩═╬╗║╚╩╩╩══╩═╩═╝╚═╬╗║╚╝░░░░░░░░░░░░░░░░
░░░░░░░░░░░░╚═╝░░░░░░░░░░░░░╚═╝░░░░░░░░░░░░░░░░░░
╔╗░╔╗░░░░░░░░╔═══╗░░░░░░░░╔═══╗░░╔╗░░░░░░░░░░░╔╗░
║║░║║░░░░░░░░║╔═╗║░░░░░░░░║╔═╗║░░║║░░░░░░░░░░░║║░
║╚═╝╠══╦╗╔╦══╣╚══╦══╦╗╔╦══╣╚═╝╠╗╔╣╚═╦╦══╦══╦═╗║║░
║╔═╗║╔╗║╚╝║║═╬══╗║╔╗║╚╝║║═╣╔╗╔╣║║║╔╗╠╣╔═╣╔╗║╔╗╬╝░
║║░║║╔╗╠╗╔╣║═╣╚═╝║╚╝║║║║║═╣║║╚╣╚╝║╚╝║║╚═╣╚╝║║║╠╗░
╚╝░╚╩╝╚╝╚╝╚══╩═══╩══╩╩╩╩══╩╝╚═╩══╩══╩╩══╩══╩╝╚╩╝░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
      """)
time.sleep(0.5)
choice = input("Hit <enter> to continue!!! ")
clear()

print("Welcome to Text Encrypter V3!\n")
time.sleep(0.5)
print("""This super simple text encrypter will let you make your secret messages look like giberish and will
      let you turn them back into words with a special key stored on your computer.""")
choice = input("Hit <enter> to start!!! ")
clear()

encrypt_menu()
