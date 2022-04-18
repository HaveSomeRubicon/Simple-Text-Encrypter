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
    return f"{':'.join([hex(chars.index(char))[2:] for char in ''.join(cipher[0])])};{':'.join([hex(chars.index(char))[2:] for char in ''.join(cipher[1])])};{cipher[2]}"


def unsimplify_cipher(cipher):
    # length = int(cipher[-1])
    # # Function to find all indexes of a character in a string

    # def find_index(string, char):
    #     output = []
    #     for char_index, str_char in enumerate(string):
    #         if str_char == char:
    #             output.append(char_index)
    #     return tuple(output)

    # # Find the index of the semi colon in the cipher
    # semicolon_indexes = find_index(cipher, ";")

    # # Extract the main key
    # main_key_hex_list = cipher[:semicolon_indexes[0]].split(":")

    # main_key_int_list = []
    # for each_hex in main_key_hex_list:
    #     main_key_int_list.append(int(each_hex, 16))

    # main_key_string = ""
    # for item in main_key_int_list:
    #     main_key_string += chars[item]
    # main_key = [main_key_string[i:i+length]
    #             for i in range(0, len(main_key_string), length)]

    # # Extract spice
    # spice_hex_list = cipher[semicolon_indexes[0] +
    #                         1:semicolon_indexes[1]].split(":")

    # spice_int_list = []
    # for each_hex in spice_hex_list:
    #     spice_int_list.append(int(each_hex, 16))

    # spice_string = ""
    # for item in spice_int_list:
    #     spice_string += chars[item]
    # spice = [''.join([chars[int(item, 16)] for item in cipher.split(';')[0].split(':')])[i:i+length] for i in range(0, len(''.join([chars[int(item, 16)] for item in cipher.split(';')[0].split(':')])), cipher[2])]
    # spice = [''.join([chars[int(item, 16)] for item in cipher.split(';')[1].split(':')])[i:i+length] for i in range(0, len(''.join([chars[int(item, 16)] for item in cipher.split(';')[0].split(':')])), cipher[2])]

    # # return normal cipher
    # return [main_key, spice, length]
    # , [''.join([chars[int(item, 16)] for item in cipher.split(';')[1].split(':')])[i:i+cipher[2]] for i in range(0, len(''.join([chars[int(item, 16)] for item in cipher.split(';')[0].split(':')])), cipher[2])], cipher[2]]
    


    
    # Non spaghetti code version is commented out above
    return [[''.join([chars[int(item, 16)] for item in cipher.split(';')[0].split(':')])[i:i+int(cipher.split(';')[2])] for i in range(0, len(''.join([chars[int(item, 16)] for item in cipher.split(';')[0].split(':')])), int(cipher.split(';')[2]))], [''.join([chars[int(item, 16)] for item in cipher.split(';')[1].split(':')])[i:i+int(cipher.split(';')[2])] for i in range(0, len(''.join([chars[int(item, 16)] for item in cipher.split(';')[1].split(':')])), int(cipher.split(';')[2]))], int(cipher.split(';')[2])]