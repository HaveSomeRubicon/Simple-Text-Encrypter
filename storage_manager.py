# ╔═╗░░░░░░╔╗░░░░░░░░░░░╔╗░░╔╗░░░░░░░░░░░░░░░░░░░░░
# ║╬╠╦╦═╦╦╦╝╠╗╔╦╗╔══╦═╗╔╝╠═╗║╚╦╦╗╔╗░░░░░░░░░░░░░░░░
# ║╔╣╔╣╬║║║╬║╚╣║║║║║║╬╚╣╬║╩╣║╬║║║╠╣░░░░░░░░░░░░░░░░
# ╚╝╚╝╚═╩═╩═╩═╬╗║╚╩╩╩══╩═╩═╝╚═╬╗║╚╝░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░╚═╝░░░░░░░░░░░░░╚═╝░░░░░░░░░░░░░░░░░░
# ╔╗░╔╗░░░░░░░░╔═══╗░░░░░░░░╔═══╗░░╔╗░░░░░░░░░░░╔╗░
# ║║░║║░░░░░░░░║╔═╗║░░░░░░░░║╔═╗║░░║║░░░░░░░░░░░║║░
# ║╚═╝╠══╦╗╔╦══╣╚══╦══╦╗╔╦══╣╚═╝╠╗╔╣╚═╦╦══╦══╦═╗║║░
# ║╔═╗║╔╗║╚╝║║═╬══╗║╔╗║╚╝║║═╣╔╗╔╣║║║╔╗╠╣╔═╣╔╗║╔╗╬╝░
# ║║░║║╔╗╠╗╔╣║═╣╚═╝║╚╝║║║║║═╣║║╚╣╚╝║╚╝║║╚═╣╚╝║║║╠╗░
# ╚╝░╚╩╝╚╝╚╝╚══╩═══╩══╩╩╩╩══╩╝╚═╩══╩══╩╩══╩══╩╝╚╩╝░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
import json
from datetime import date
import cipher_tools
import pprint
today = date.today()


def format_json(path="my_stuff.json"):
    with open(path, 'r') as json_file:
        json_data = json.loads(json_file.read())
    with open(path, 'w') as json_file:
        json_file.write(pprint.pformat(json_data).replace("'", '"'))


def reset_json(path="my_stuff.json"):
    with open(path, "w") as file:
        file.write('{"ciphers": [], "myEncryptedText": []}')
    format_json()


def read_json(path="my_stuff.json"):
    with open(path, "r") as json_file:
        return json.load(json_file)
    format_json()


def write_to_json(file_to_write, destination="my_stuff.json"):
    with open(destination, "w") as file:
        json.dump(file_to_write, file)
    format_json()



def append_cipher(title, cipher, path="my_stuff.json", date=today.strftime("%B %d, %Y")):
    json_file = read_json(path)
    json_file["ciphers"].append(
        {"title": title, "date": date, "cipher": cipher})
    write_to_json(json_file, path)
    format_json()



def append_encrypted_text(title, encrypted_text, path="my_stuff.json", date=today.strftime("%B %d, %Y")):
    new_json = read_json()
    new_json["myEncryptedText"].append(
        {"title": title, "encryptedText": encrypted_text, 'date': date})
    write_to_json(new_json)
    format_json()


def run_checks():
    try:
        with open("my_stuff.json", "r") as json_file:
            if json_file.read() == '' or json_file.read() == 'none':
                reset_json()
    except FileNotFoundError:
        reset_json()
    format_json()


if __name__ == "__main__":
    input("WARNING: IF YOU ARE SEEING THIS YOU ARE MOST LIKELY RUNNING THE WRONG SCRIPT!!! PLEASE RUN main.py INSTEAD OF THIS SCRIPT")
    input("Press enter if you are purposefully running this script and you know what your doing: ")
    if input("Would you like to reset the json file[Y or N]?: ").lower() == 'y':
        reset_json()
