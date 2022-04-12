import time
import encryption_tools
import storage_manager
import cipher_tools
import os
import json
import subprocess

# Run checks to see if json files are empty or dont exist
storage_manager.run_checks()

def clear(): return subprocess.run(['cls' if os.name == 'nt' else 'clear'])

# Define menu functions
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
    # Key selector function
    def key_selector(title="Select a key: "):
        clear()
        sprint(title)
        ciphers = storage_manager.read_json()['ciphers']
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
            if not int(key_choice) < 1:
                return ciphers[int(key_choice) - 1]
            else:
                sprint(
                    "Oops, that number is not a key! ERROR: Less than lowest index key")
                enter_menu()
                return key_selector()
        except:
            sprint(
                "Oops, that number is not a key! ERROR: Greater than highest index key")
            enter_menu()
            return key_selector()

    # Display options
    clear()
    print("""
╔═╗╔═╗
║║╚╝║║
║╔╗╔╗╠══╦╦═╗─╔╗╔╦══╦═╗╔╗╔╦╗
║║║║║║╔╗╠╣╔╗╗║╚╝║║═╣╔╗╣║║╠╝
║║║║║║╔╗║║║║║║║║║║═╣║║║╚╝╠╗
╚╝╚╝╚╩╝╚╩╩╝╚╝╚╩╩╩══╩╝╚╩══╩╝""")
    time.sleep(0.1)
    print("Press E and hit <enter> to encrypt text")
    time.sleep(0.1)
    print("Press D and hit <enter> to decrypt text")
    time.sleep(0.1)
    print("Press M and hit <enter> to make a new key")
    time.sleep(0.1)
    print("Press K and hit <enter> to list all your keys")
    time.sleep(0.1)
    print("Press I and hit <enter> to import a key")
    time.sleep(0.1)
    print("Press X and hit <enter> to export a key")
    time.sleep(0.1)
    print("Press F and hit <enter> to delete a key")
    time.sleep(0.1)
    print("Press Q and hit <enter> to quit program")
    time.sleep(0.1)
    print('')

    # Take input
    try:
        menu_choice = input(
            "Enter the letter that corresponds with the option of your choice: ")[0].upper()
    except IndexError:
        menu()
        return ''
    if menu_choice == 'E':
        clear()
        # Let the user choose a key and convert it to raw format
        cipher = cipher_tools.unsimplify_cipher(key_selector()['cipher'])
        text_input = input("What text would you like to encrypt?:\n")
        clear()
        sprint("Your encrypted text: \n")
        sprint(encryption_tools.encrypt(text_input, cipher), speed=0.01)  # Encrypt
        print('')
        enter_menu()
    elif menu_choice == 'D':
        clear()
        # Let the user choose a key and convert it to raw format
        cipher = cipher_tools.unsimplify_cipher(key_selector()['cipher'])
        text_input = input("What text would you like to decrypt?:\n")
        clear()
        sprint("Your decrypted text: \n")
        sprint(encryption_tools.decrypt(text_input, cipher), speed=0.01)  # Decrypt
        print('')
        enter_menu()
    elif menu_choice == 'M':
        clear()
        title_input = ''
        while title_input == '':
            sprint("What would you like to call this new key?: ", end='')
            title_input = input()
            if title_input == '':
                sprint("Please give you key a name!")
                clear()
        storage_manager.append_cipher(
            title_input, cipher_tools.simplify_cipher(cipher_tools.make_cipher()))
        sprint(
            "New key was succesfully made! You may now use this key to encrypt and decrypt text!")
        enter_menu()
    elif menu_choice == 'K':
        clear()
        sprint("Your keys:")
        ciphers = storage_manager.read_json()['ciphers']
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
        clear()
        sprint("Rename the export.txt file to import.txt and place the file in the same folder this script is in and press enter when your done.")
        enter_menu()
        if not os.path.isfile('import.txt'):  # Check if an import.txt file exists
            clear()
            sprint("The program wasn't able to find a import.txt file. Did you place it in the same folder this script is in?")
            enter_menu()
            menu()
            return ''
        try:
            storage_manager.append_cipher(storage_manager.read_json('import.txt')['title'], storage_manager.read_json(
                'import.txt')['cipher'], date=storage_manager.read_json('import.txt')['date'])  # Add the cipher from import.txt
            sprint("The key was succesfully added!")
        except:
            sprint("The import.txt file was found but the program was not able to read it. Make sure it hasn't been tampered with.")
        enter_menu()
    elif menu_choice == 'X':
        export_key = key_selector("What key would you like to export?: ")
        storage_manager.write_to_json(export_key, "export.txt")
        sprint("The key has been exported to the export.txt file.")
        enter_menu()
    elif menu_choice == 'F':
        deleted_key = key_selector("What key would you like to delete: ")

        if input(f"PRESS <enter> IF YOU ARE SURE ABOUT DELETING {deleted_key['title']}(1), PRESS Q AND HIT <enter> TO QUIT:") == '':
            if input(f"PRESS <enter> IF YOU ARE SURE ABOUT DELETING {deleted_key['title']}(2), PRESS Q AND HIT <enter> TO QUIT:") == '':
                if input(f"PRESS <enter> IF YOU ARE SURE ABOUT DELETING {deleted_key['title']}(3), PRESS Q AND HIT <enter> TO QUIT:") == '':
                    pass
                else:
                    menu()
                    return ''
            else:
                menu()
                return ''
        else:
            menu()
            return ''
        json_file = storage_manager.read_json()
        json_file['ciphers'].remove(deleted_key)
        storage_manager.write_to_json(json_file)
        sprint("The key was succesfully deleted.")
        enter_menu()
    elif menu_choice == 'Q':
        clear()
        quit()
    else:
        sprint("That option does not exist!")
        enter_menu()
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
