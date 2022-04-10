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
import cipher_utils
today = date.today()


def reset_json(path="cipher.json"):
    with open(path, "w") as file:
        file.write('{"ciphers": []}')


def read_ciphers(path="cipher.json"):
    with open(path, "r") as json_file:
        return json.load(json_file)


def write_to_ciphers(file_to_write, destination="cipher.json"):
    with open(destination, "w") as file:
        json.dump(file_to_write, file)


def append_cipher_to_ciphers(title, cipher, path="cipher.json", date=today.strftime("%B %d, %Y")):
    json_file = read_ciphers(path)
    json_file["ciphers"].append(
        {"title": title, "date": date, "cipher": cipher})
    write_to_ciphers(json_file, path)
