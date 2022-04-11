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
import random
from textwrap import wrap as group_chars
chars = [
    item for item in """`1234567890-=~!@#$%^&*()_+qwertyuiop[]\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>?äëïöüÿÄËÏÖÜŸáćéíńóśúýźÁĆÉÍŃÓŚÚÝŹőűŐŰàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛãñõÃÑÕčďěǧňřšťžČĎĚǦŇŘŠŤŽđĐåůÅŮąęĄĘæÆøØçÇłŁßþżŻäëïöüÿÄËÏÖÜŸáćéíńóśúýźÁĆÉÍŃÓŚÚÝŹőűŐŰàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛãñõÃÑÕčďěǧňřšťžČĎĚǦŇŘŠŤŽđĐåůÅŮąęĄĘæÆøØçÇłŁßþżŻαΑβΒγΓδΔεΕζΖηΗθΘϑικΚλΛμΜνΝξΞοΟπΠρΡσΣςτυΥφΦϕχΧψΨωΩ """]
chars_no_space = [item for item in chars if not item == " "]


def make_cipher(length=4):
    cipher = [[], ["" for _ in range(100)], length]
    # main key, spice and length
    used_values = []

    # Function to make a random string
    def random_string():
        output = ""
        for _ in range(length):
            random_choice = random.choice(chars_no_space)
            output = output + random_choice
            while output in used_values:
                random_choice = random.choice(chars_no_space)
                output = output[0:-length] + random_choice
        used_values.append(output)
        return output

    # Make the main portion of the key
    for _ in chars:
        cipher[0].append(random_string())

    # Make the salt
    i = 0
    for item in cipher[1]:
        cipher[1][i] = random_string()
        i += 1

    return cipher


def simplify_cipher(cipher):
    main_key_raw = cipher[0]
    spices_raw = cipher[1]
    length = cipher[2]

    # main_key_raw -> string
    main_key_string = ""
    for item in main_key_raw:
        main_key_string += item

    # main_key_string -> hex
    main_key_hex_list = []
    for char in main_key_string:
        char_int = chars.index(char)
        # copied from https://stackoverflow.com/a/12638477
        char_hex = (f"{char_int:#0{5}x}"[2:])
        main_key_hex_list.append(char_hex)
    main_key_hex = ':'.join(main_key_hex_list)

    # spice -> string
    spice_string = ""
    for item in spices_raw:
        spice_string += item

    # spice_string -> hex
    spice_hex_list = []
    for char in spice_string:
        char_int = chars.index(char)
        # copied from https://stackoverflow.com/a/12638477
        char_hex = (f"{char_int:#0{5}x}"[2:])
        spice_hex_list.append(char_hex)
    spice_hex = ":".join(spice_hex_list)

    return f"{main_key_hex};{spice_hex};{length}"


def unsimplify_cipher(cipher):
    length = int(cipher[-1])
    # Function to find all indexes of a character in a string

    def find_index(string, char):
        output = []
        for char_index, str_char in enumerate(string):
            if str_char == char:
                output.append(char_index)
        return tuple(output)

    # Find the index of the semi colon in the cipher
    semicolon_indexes = find_index(cipher, ";")

    # Extract the main key
    main_key_hex_list = cipher[:semicolon_indexes[0]].split(":")

    main_key_int_list = []
    for each_hex in main_key_hex_list:
        main_key_int_list.append(int(each_hex, 16))

    main_key_string = ""
    for item in main_key_int_list:
        main_key_string += chars[item]
    main_key = [main_key_string[i:i+length]
                for i in range(0, len(main_key_string), length)]

    # Extract spice
    spice_hex_list = cipher[semicolon_indexes[0] +
                            1:semicolon_indexes[1]].split(":")

    spice_int_list = []
    for each_hex in spice_hex_list:
        spice_int_list.append(int(each_hex, 16))

    spice_string = ""
    for item in spice_int_list:
        spice_string += chars[item]
    spice = [spice_string[i:i+length]
             for i in range(0, len(spice_string), length)]

    # return normal cipher
    return [main_key, spice, length]