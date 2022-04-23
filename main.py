import time
import encryption_tools
import storage_manager
import cipher_tools
import os
import json
import subprocess
import tkinter as tk
  

window = tk.Tk()
shat = lambda: print('hi')
def main_menu():
    encrypt_button = tk.Button(window, text = 'Encrypt')
    decrypt_button = tk.Button(window, text = 'Decrypt')
    list_key_button = tk.Button(window, text = 'List keys')
    make_key_button = tk.Button(window, text = 'Make key')
    
    
    encrypt_button.pack()
    decrypt_button.pack()  
    list_key_button.pack()
    make_key_button.pack()
main_menu()

window.mainloop()