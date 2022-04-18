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


def reset_json(path="my_stuff.json"):
    with open(path, "w") as file:
        file.write('{"ciphers": []}')


def read_json(path="my_stuff.json"):
    with open(path, "r") as json_file:
        return json.load(json_file)


def write_to_json(file_to_write, destination="my_stuff.json"):
    with open(destination, "w") as file:
        json.dump(file_to_write, file)


def append_cipher(title, cipher, path="my_stuff.json", date=today.strftime("%B %d, %Y")):
    json_file = read_json(path)
    json_file["ciphers"].append(
        {"title": title, "date": date, "cipher": cipher})
    write_to_json(json_file, path)


def run_checks():
    try:
        with open("my_stuff.json", "r") as json_file:
            if json_file.read() == '' or json_file.read() == 'none':
                reset_json()
    except FileNotFoundError:
        reset_json()


if __name__ == "__main__":
    input("WARNING: IF YOU ARE SEEING THIS YOU ARE MOST LIKELY RUNNING THE WRONG SCRIPT!!! PLEASE RUN main.py INSTEAD OF THIS SCRIPT")
    input("Press enter if you are purposefully running this script and you know what your doing: ")
    if input("Would you like to reset the json file[Y or N]?: ").lower() == 'y':
        reset_json()
