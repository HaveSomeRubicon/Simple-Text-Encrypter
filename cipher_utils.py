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
        char_hex = (f"{char_int:#0{5}x}"[2:]) # copied from https://stackoverflow.com/a/12638477
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
        char_hex = (f"{char_int:#0{5}x}"[2:]) # copied from https://stackoverflow.com/a/12638477
        spice_hex_list.append(char_hex)
    spice_hex = ":".join(spice_hex_list)
    
    return f"{main_key_hex};{spice_hex};{length}"

def unsimplify_cipher(cipher):
    pass