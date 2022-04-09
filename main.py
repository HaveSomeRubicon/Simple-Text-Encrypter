import time
import encrypter
import json_utils
import cipher_utils
import os

# Check if cipher.json is empty
try:
    with open("cipher.json", "r") as json_file:
        if json_file.read() == '':
            json_utils.reset_json()
except FileNotFoundError:
    json_utils.reset_json()

def clear(): return os.system("clear")


def sprint(text, speed=0.06, wait=0, end='\n'):
    for each_char in text:
        print(each_char, flush=True, end='')
        time.sleep(speed)
    time.sleep(wait)
    print('', end=end)


def enter_menu():
    sprint("Press <enter> to continue", end='')
    input("")


def menu():
    def key_selector(title="Select a key: "):
        clear()
        sprint(title)
        ciphers = json_utils.export_json_file()['ciphers']
        time.sleep(0.2)
        if ciphers == []:
            print(
                "Oops, looks like you have no keys! Please go to the main menu and create a new key.")
            enter_menu()
            menu()
            return
        for item in ciphers:
            print(
                f'{ciphers.index(item) + 1}. "{item["title"]}" created on {item["date"]}')
            time.sleep(0.1)
            if item == ciphers[-1]:
                last_index = ciphers.index(item)
        key_choice = input(
            f"\nChoose a key(1-{ciphers.index(item) + 1})?: ")
        try:
            return ciphers[int(key_choice) - 1]
        except:
            sprint("Oops, that number does not exist!")
            enter_menu()
            return key_selector()

    clear()
    print("""
╔═╗╔═╗
║║╚╝║║
║╔╗╔╗╠══╦╦═╗─╔╗╔╦══╦═╗╔╗╔╦╗
║║║║║║╔╗╠╣╔╗╗║╚╝║║═╣╔╗╣║║╠╝
║║║║║║╔╗║║║║║║║║║║═╣║║║╚╝╠╗
╚╝╚╝╚╩╝╚╩╩╝╚╝╚╩╩╩══╩╝╚╩══╩╝""")
    time.sleep(0.2)
    print("Press E and hit <enter> to encrypt text")
    time.sleep(0.2)
    print("Press D and hit <enter> to decrypt text")
    time.sleep(0.2)
    print("Press M and hit <enter> to make a new key")
    time.sleep(0.2)
    print("Press K and hit <enter> to list all your keys")
    time.sleep(0.2)
    print("Press I and hit <enter> to import a key")
    time.sleep(0.2)
    print("Press X and hit <enter> to export a key")
    time.sleep(0.2)
    print("Press F and hit <enter> to delete a key")
    time.sleep(0.2)
    print("Press Q and hit <enter> to quit program")
    time.sleep(0.2)
    print('')

    menu_choice = input(
        "Enter the letter that corresponds with the option of your choice: ")[0].upper()
    if menu_choice == 'E':
        clear()
        cipher = cipher_utils.unsimplify_cipher(key_selector()['cipher'])
        text_input = input("What text would you like to encrypt?:\n")
        clear()
        sprint("Your encrypted text: \n")
        sprint(encrypter.encrypt(text_input, cipher), speed=0.01)
        print('')
        enter_menu()
    elif menu_choice == 'D':
        clear()
        cipher = cipher_utils.unsimplify_cipher(key_selector()['cipher'])
        text_input = input("What text would you like to decrypt?:\n")
        clear()
        sprint("Your decrypted text: \n")
        sprint(encrypter.decrypt(text_input, cipher), speed=0.01)
        print('')
        enter_menu()
    elif menu_choice == 'M':
        clear()
        sprint("What would you like to call this new key?: ", end='')
        title_input = input()
        json_utils.append_cipher(
            title_input, cipher_utils.simplify_cipher(cipher_utils.make_cipher()))
        sprint(
            "New key was succesfully made! You may now use this key to encrypt and decrypt text!")
        enter_menu()
    elif menu_choice == 'K':
        clear()
        sprint("Your keys:")
        ciphers = json_utils.export_json_file()['ciphers']
        time.sleep(0.2)
        if ciphers == []:
            print(
                "Oops, looks like you havent made a key yet! Please go to the main menu and create a new key.")
            enter_menu()
            menu()
            return
        for item in ciphers:
            print(
                f'{ciphers.index(item) + 1}. "{item["title"]}" created on {item["date"]}')
            time.sleep(0.1)
            if item == ciphers[-1]:
                last_index = ciphers.index(item)
        print('')
        enter_menu()
    elif menu_choice == 'I':
        import_key = dict(input("Please copy paste in an exported key. If your exported key is in a file open it and copy paste the contents into this program: "))
        json_utils.append_cipher(
            import_key['title'], import_key['cipher'], import_key['date'])
        print(export_key)
    elif menu_choice == 'X':
        export_key = key_selector("What key would you like to export?: ")
        with open("export.txt", "w") as export_file:
            export_file.write(str(export_key))
        sprint('The key has been exported to the export.txt file.')
        enter_menu()
    elif menu_choice == 'F':
        deleted_key = key_selector("What key would you like to delete: ")
        exported_keys = json_utils.export_json_file()
        input(f"PRESS <enter> IF YOU ARE SURE ABOUT DELETING {deleted_key['title']}(1):")
        input(f"PRESS <enter> IF YOU ARE SURE ABOUT DELETING {deleted_key['title']}(2):")
        input(f"PRESS <enter> IF YOU ARE SURE ABOUT DELETING {deleted_key['title']}(3):")
        exported_keys['ciphers'].remove(deleted_key)
        json_utils.write_json_file(exported_keys)
        sprint("The key was succesfully deleted.")
        enter_menu()
    elif menu_choice == 'Q':
        clear()
        quit()
    menu()


# Welcome screen:
# clear()
# print("WARNING: This is NOT a profesional encrypter and was only made as practice for the developer!")
# print("""░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗██╗██╗██╗
# ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝██║██║██║
# ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░██║██║██║
# ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░╚═╝╚═╝╚═╝
# ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗██╗██╗██╗
# ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝╚═╝╚═╝""")
# sprint("Welcome to Text Encrypter V3!", wait=0.2)
# sprint("""This program can take any text and scramble it up into a gibberish message that can be turned back into normal text with a special "key"
# that is stored on your computer. You can share this key with you friends too if you want them to be able to decode your message.""", wait=0.2)
# enter_menu()
# Main menu loop
menu()
