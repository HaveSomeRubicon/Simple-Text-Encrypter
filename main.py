from msilib.schema import RadioButton
import time
import encryption_tools
import storage_manager as st
import cipher_tools
import os
import json
import subprocess
import tkinter as tk

root = tk.Tk()

# Define main menu functions


def destroy_widgets():
    for widget in root.winfo_children():
        widget.destroy()

def key_selector(title_text = 'Select a key to use: '):
    title_widget = tk.Label(
        root, 
        text='Type in some text that you want to encrypt: ', 
        wraplength=200,
        font=('Arial', 15))
    w = tk.RadioButton(root, text='Hello!')
    
    title_widget.grid(row=0, column=1)
    w.grid(row=1, column=2)
    
    
def encrypt_menu():
    key_selector()
    # title_widget = tk.Label(
    #     root, 
    #     text='Type in some text that you want to encrypt: ', 
    #     wraplength=200,
    #     font=('Arial', 15))
    # text_entry = tk.Entry(root)
    # def submit(): 
    #     encrypted_text = tk.Text(encryption_tools.encrypt(text_entry.get()))
    #     encrypted_text.grid(row=3,column=1)
    # submit_button = tk.Button(root, text="Done", font=('Arial', 20), command=submit)
    
    
    # title_widget.grid(row=0, column=1, sticky='w')
    # text_entry.grid(row=1, column=1, ipady=8, ipadx=22, sticky='w')
    # submit_button.grid(row=2, column=1, ipadx=47, sticky='w')


def main_menu():
    destroy_widgets()
    options = (("Encrypt", encrypt_menu), ("Decrypt", None),
               ("List Keys", None), ("Make key", None))
    for button in options:
        menu_button = tk.Button(root, text=button[0], font=(
            'Arial', 20), width=10, command=button[1])
        if(options.index(button) != 0):
            menu_button.grid(row=options.index(button), padx=5)
        else:
            menu_button.grid(row=options.index(button), padx=5, pady=(5, 0))


main_menu()
root.mainloop()
