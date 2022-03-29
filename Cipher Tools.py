from random import *

def make_cipher():
    empty_cipher = {
        "a": """""",
        "b": """""",
        "c": """""",
        "d": """""",
        "e": """""",
        "f": """""",
        "g": """""",
        "h": """""",
        "i": """""",
        "j": """""",
        "k": """""",
        "l": """""",
        "m": """""",
        "n": """""",
        "o": """""",
        "p": """""",
        "q": """""",
        "r": """""",
        "s": """""",
        "t": """""",
        "u": """""",
        "v": """""",
        "w": """""",
        "x": """""",
        "y": """""",
        "z": """""",
        "A": """""",
        "B": """""",
        "C": """""",
        "D": """""",
        "E": """""",
        "F": """""",
        "G": """""",
        "H": """""",
        "I": """""",
        "J": """""",
        "K": """""",
        "L": """""",
        "M": """""",
        "N": """""",
        "O": """""",
        "P": """""",
        "Q": """""",
        "R": """""",
        "S": """""",
        "T": """""",
        "U": """""",
        "V": """""",
        "W": """""",
        "X": """""",
        "Y": """""",
        "Z": """""",
    }
    for key in empty_cipher:
        chars_list = ("""`1234567890-=~!@#$&*()_+qwertyuiop[]QWERTYUIOP|asdfghjkl;'ASDFGHJKL:"zxcvbnm,.ZXCVBNM<>?""")
        the_what = f"%{choice(chars_list)}{choice(chars_list)}{choice(chars_list)}{choice(chars_list)}^"
        empty_cipher[key] = the_what
    return empty_cipher
def compress_cipher(decompressed_cipher):
    # Create a list with each value from the cipher
    cipher_keys_list = []
    for each_key in decompressed_cipher.values():
        cipher_keys_list.append(each_key[1:5])
    
    # Break up each character of the cipher values into a matrix
    cipher_keys_list_chars = []
    for each_key in cipher_keys_list:
        current_key_chars = []
        for each_char in each_key:
            current_key_chars.append(each_char)
        cipher_keys_list_chars.append(current_key_chars)
    
    # Convert each char in the matrix to a matrix of hex values
    char_to_decimal = """`1234567890-=~!@#$&*()_+qwertyuiop[]QWERTYUIOP|asdfghjkl;'ASDFGHJKL:"zxcvbnm,.ZXCVBNM<>?"""
    hex_key_matrix = []
    for each_list in cipher_keys_list_chars:
        current_key_chars = []
        for each_char in each_list:
            current_key_chars.append(hex(char_to_decimal.index(each_char))[2:])
        hex_key_matrix.append(current_key_chars)
    
    # Convert the matrix of hex values to one fat string
    compressed_cipher = '^'
    for each_list in hex_key_matrix:
        for each_hex in each_list:
            compressed_cipher = compressed_cipher + each_hex + '^'
    return compressed_cipher
def make_and_compress_cipher():
    return compress_cipher(make_cipher())
def decompress_cipher(cipher):
    # Convert string of hex values to a list of hex values
    hex_values = []
    for char in cipher:
        if char == '^':
            hex_values.append('')
        else:
            hex_values[-1] = hex_values[-1] + char
    hex_values.pop(-1)

    # Convert hex values list to decimal values list
    decimal_values = []
    for hex_value in hex_values:
        decimal_values.append(int(hex_value, 16))
    
    # Convert decimal values to letters
    decimal_to_chars = """`1234567890-=~!@#$&*()_+qwertyuiop[]QWERTYUIOP|asdfghjkl;'ASDFGHJKL:"zxcvbnm,.ZXCVBNM<>?"""
    individual_chars = ''
    for item in decimal_values: 
        individual_chars += decimal_to_chars[item]

    # Convert letters to list of 4 grouped chars
    grouped_chars = []
    i = 0
    for char in individual_chars:
        if i % 4 == 0:
            grouped_chars.append('')
            grouped_chars[-1] += char
        else:
            grouped_chars[-1] += char
        i += 1

    # Finally add the values to a dictionary
    decompressed_cipher = {
        "a": """""",
        "b": """""",
        "c": """""",
        "d": """""",
        "e": """""",
        "f": """""",
        "g": """""",
        "h": """""",
        "i": """""",
        "j": """""",
        "k": """""",
        "l": """""",
        "m": """""",
        "n": """""",
        "o": """""",
        "p": """""",
        "q": """""",
        "r": """""",
        "s": """""",
        "t": """""",
        "u": """""",
        "v": """""",
        "w": """""",
        "x": """""",
        "y": """""",
        "z": """""",
        "A": """""",
        "B": """""",
        "C": """""",
        "D": """""",
        "E": """""",
        "F": """""",
        "G": """""",
        "H": """""",
        "I": """""",
        "J": """""",
        "K": """""",
        "L": """""",
        "M": """""",
        "N": """""",
        "O": """""",
        "P": """""",
        "Q": """""",
        "R": """""",
        "S": """""",
        "T": """""",
        "U": """""",
        "V": """""",
        "W": """""",
        "X": """""",
        "Y": """""",
        "Z": """""",
    }
    
    iterator = 0
    for item in decompressed_cipher:
        decompressed_cipher[item] = '%' + grouped_chars[iterator] + '^'
        iterator += 1
    return decompressed_cipher