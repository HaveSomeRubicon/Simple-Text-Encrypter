import random

def make_key(key_value_length):
    # Create template objects
    salt_template = {"salt1": """""","salt2": """""","salt3": """""","salt4": """""","salt5": """""","salt6": """""","salt7": """""","salt8": """""","salt9": """""","salt10": """""","salt11": """""","salt12": """""","salt13": """""","salt14": """""","salt15": """""","salt16": """""","salt17": """""","salt18": """""","salt19": """""","salt20": """""",}
    oe_chars_template = {"opening": """""", "ending": """"""}
    list_of_chars = [' ','`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']
    list_of_chars_no_space = [item for item in list_of_chars if item != ' ']
    # Create the template for the main key 
    main_key_template = {}
    for new_key in list_of_chars:
        main_key_template[new_key] = ""

    # Create key opening and ending characters
    oe_chars = {"opening": """""", "ending": """"""}
    for item in oe_chars_template:
        oe_chars[item] = random.choice(list_of_chars_no_space)
    
    # Create a empty list which will contain used values from the key
    used_values = []
    
    # Create salt
    temp_salt_value = ""
    salt = salt_template
    for key_value in salt_template:
        # Start over if the new value exists somewhere
        temp_salt_value = ""
        while not temp_salt_value in used_values:
            temp_salt_value = oe_chars["opening"]
            # Repeat the given amount of times to create each individual value char
            for item in range(key_value_length):
                temp_salt_value = temp_salt_value + random.choice(list_of_chars)
            temp_salt_value = temp_salt_value + oe_chars["ending"]
            if not temp_salt_value in used_values:
                used_values.append(temp_salt_value)
        salt[key_value] = temp_salt_value
        
    # Generate the main key
    main_key = main_key_template
    for each_key in main_key_template:
        temp_new_key = ""
        while not temp_new_key in used_values:
            temp_new_key = oe_chars['opening']
            for lagit_why_u_readin_dis_boi in range(key_value_length):
                temp_new_key = temp_new_key + random.choice(list_of_chars)
            temp_new_key = temp_new_key + oe_chars["ending"]
            if not temp_new_key in used_values:
                used_values.append(temp_new_key)
                break
        main_key[each_key] = temp_new_key
    
    # Create the final key
    final_key = [oe_chars, main_key, salt] # Format: oe_chars, main_key, salt
    
    return final_key
# def compress_key(input_key):
#     # Individualise each item of the key
#     oe_chars = input_key[0]
#     main_key = input_key[1]
#     salt = input_key[2]
