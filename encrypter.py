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
chars = [item for item in """`1234567890-=~!@#$%^&*()_+qwertyuiop[]\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>?äëïöüÿÄËÏÖÜŸáćéíńóśúýźÁĆÉÍŃÓŚÚÝŹőűŐŰàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛãñõÃÑÕčďěǧňřšťžČĎĚǦŇŘŠŤŽđĐåůÅŮąęĄĘæÆøØçÇłŁßþżŻäëïöüÿÄËÏÖÜŸáćéíńóśúýźÁĆÉÍŃÓŚÚÝŹőűŐŰàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛãñõÃÑÕčďěǧňřšťžČĎĚǦŇŘŠŤŽđĐåůÅŮąęĄĘæÆøØçÇłŁßþżŻαΑβΒγΓδΔεΕζΖηΗθΘϑικΚλΛμΜνΝξΞοΟπΠρΡσΣςτυΥφΦϕχΧψΨωΩ """]
chars_no_space = [item for item in chars if not item == " "]


def encrypt(text, cipher):
    main_key_raw = cipher[0]
    spices = cipher[1]
    length = cipher[2]

    # Make main key dictionary
    main_key = {}
    for key in main_key_raw:
        main_key[chars[main_key_raw.index(key)]] = key

    # Encrypt the text
    encrypted = ""
    for char in text:
        if random.randint(1, 3) == 1:
            encrypted = encrypted + random.choice(spices)
            if random.randint(1, 3) == 1:
                encrypted = encrypted + random.choice(spices)
                if random.randint(1, 3) == 1:
                    encrypted = encrypted + random.choice(spices)
        try:
            encrypted = encrypted + main_key[char]
        except KeyError:
            print(
                f"EEROR: Unsupported character '{char}', the character will be skipped.")
    if random.randint(1, 3) == 1:
        encrypted = encrypted + random.choice(spices)
        if random.randint(1, 3) == 1:
            encrypted = encrypted + random.choice(spices)
            if random.randint(1, 3) == 1:
                encrypted = encrypted + random.choice(spices)

    return encrypted


def decrypt(encrypted, cipher):
    # Split up the cipher into diffrent lists, vars, etc
    spices = cipher[1]
    length = cipher[2]
    main_key = {}
    for key in cipher[0]:
        main_key[chars[cipher[0].index(key)]] = key
    inv_main_key = {v: k for k, v in main_key.items()}

    # Split up the encrypted text into its individual encrypted letters
    i = 0
    divided_up_encrypted = []
    for item in encrypted:
        if i % length == 0:
            divided_up_encrypted.append("")
            divided_up_encrypted[-1] = divided_up_encrypted[-1] + item
        else:
            divided_up_encrypted[-1] = divided_up_encrypted[-1] + item
        i += 1

    # Convert encrypted letters to text
    decrypted = ""
    spice_counter = 0
    for item in divided_up_encrypted:
        try:
            decrypted = decrypted + inv_main_key[item]
        except KeyError:
            spice_counter += 1

    return decrypted
