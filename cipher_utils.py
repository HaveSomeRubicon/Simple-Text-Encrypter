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


def shrinkify_cipher(cipher):
    main_key_raw = cipher[0]
    salt_raw = cipher[1]
    length = cipher[2]
    output = length + ""

    # Append main keys values to output
    for item in main_key_raw:
        output = output + item
        
    
    

haxed = shrinkify_cipher(make_cipher())
print(haxed)
