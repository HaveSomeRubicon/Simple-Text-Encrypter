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
today = date.today()


def reset_json(path="my_stuff.json"):
    with open(path, "w") as file:
        file.write('{"ciphers": [], "myEncryptedText": []}')


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


def append_encrypted_text(title, encrypted_text, path="my_stuff.json"):
    new_json = read_json()
    new_json["myEncryptedText"].append(
        {"title": title, "encryptedText": encrypted_text})
    write_to_json(new_json)


def run_checks():
    try:
        with open("my_stuff.json", "r") as json_file:
            if json_file.read() == '':
                reset_json()
    except FileNotFoundError:
        reset_json()
