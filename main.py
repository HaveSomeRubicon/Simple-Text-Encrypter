import cipher_tools

def encrypt(raw_text, decrypted_key, dev_mode = False):
    # Individualise the keys sub-groups
    oe_chars = decrypted_key[0]
    main_key = decrypted_key[1]
    salt = decrypted_key[2]
    
    # Figure out the key value length
    key_value_length = len(main_key['a']) - 2
    
    # Convert string(the text inputted) to a list of each char
    text = [item for item in raw_text]
    
    # Finally encrypt each letter one by one
    encrypted_output = ''
    for item in text:
        try:
            if dev_mode: print(f"letter {item} was encrypted to {main_key[item]}")
            encrypted_output = encrypted_output + main_key[item]
        except KeyError:
            if dev_mode: print(f"letter '{item}' could not be added to encrypted_output")
            encrypted_output = encrypted_output + item
        encrypted_output = encrypted_output
    
    return encrypted_output

print(encrypt("Hello world you are beautiful yet cruel", cipher_tools.make_key(4), True))
