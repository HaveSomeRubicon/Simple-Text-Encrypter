import time
import encryption_tools
import storage_manager
import cipher_tools
import os
import json
import subprocess

# Run checks to see if json files are empty or dont exist
storage_manager.run_checks()


# Define menu functions
def clear(): return subprocess.run(['cls' if os.name == 'nt' else 'clear'])


def sprint(text, speed=0.06, wait=0, end='\n'):
    for each_char in text:
        print(each_char, flush=True, end='')
        time.sleep(speed)
    time.sleep(wait)
    print('', end=end)


def sinput(text, speed=0.06, wait=0, end='\n'):
    sprint(text, speed, wait, end='')
    return input("")


def enter_menu():
    sinput("Press <enter> to continue")


def menu(welcome_text=False):
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
        key_choice = sinput(
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

    
    # Encrypted text selector(WIP)
    # def encrypted_text_selector(title = "Select a encrypted text: "):
    #     clear()
    #     sprint(title)
        
    # Display options
    clear()
    print("""
╔═╗╔═╗
║║╚╝║║
║╔╗╔╗╠══╦╦═╗─╔╗╔╦══╦═╗╔╗╔╦╗
║║║║║║╔╗╠╣╔╗╗║╚╝║║═╣╔╗╣║║╠╝
║║║║║║╔╗║║║║║║║║║║═╣║║║╚╝╠╗
╚╝╚╝╚╩╝╚╩╩╝╚╝╚╩╩╩══╩╝╚╩══╩╝""")
    if welcome_text:
        print("""Welcome to Simple-Text-Encrypter V3, this program can take any text and scramble it up into a gibberish message that can be turned backinto normal text with a special "key" that is stored on your computer. You can share this key with you friends too if you want them to be able to decode your message.""")
        print("-------------------------------------------------------------------")
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
        selected_cipher = cipher_tools.unsimplify_cipher(
            key_selector()['cipher'])
        encrypted_text = encryption_tools.encrypt(
            sinput("What text would you like to encrypt?: "), selected_cipher)
        clear()
        sprint("Your encrypted text: \n", wait=0.2)
        sprint(encrypted_text + '\n', speed=0.01, wait=0.2)
        sprint("If you want to copy it higlight the encrypted text and press CTRL+SHIFT+C(not CTRL+C!!!) to copy it.", speed=0.05, wait=0.2)
        if sinput("Would you like to save this encrypted text[Y or N]?: ", wait=0.2).lower() == 'y':
            storage_manager.append_encrypted_text(sinput(
                "What would you like to call this encrypted text?: ", wait=0.2), encrypted_text)
            sprint("Encrypted text was succesfully saved!")
        enter_menu()
    elif menu_choice == 'D':
        clear()
        selected_cipher = cipher_tools.unsimplify_cipher(
            key_selector()['cipher'])
        decrypted_text = encryption_tools.decrypt(sinput(
            "Paste in some text that was encrypted with the same key by pressing CTRL+SHIFT+V(not CTRL+V!!!): ", speed=0.05), selected_cipher)
        clear()
        sprint("Your decrypted text: \n")
        sprint(decrypted_text + '\n', speed=0.01)
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


menu(True)
