import time
import encryption_tools
import storage_manager as st
import cipher_tools
import os
import json
import subprocess
import tkinter as tk
selected_key = None

root = tk.Tk()


def destroy_widgets():
    for widget in root.winfo_children():
        widget.destroy()


def key_selector(title_text='Select a key to use: '):
    global selected_key
    selected_key = None
    selected_key_index = tk.IntVar()

    title_widget = tk.Label(root, text=title_text, wraplength=200, font=(
        'Arial', 15))
    title_widget.grid(row=0, column=1, sticky='w')

    def submit_key():
        global selected_key
        selected_key = st.read_json()['ciphers'][selected_key_index.get()]

    for index, key in enumerate(st.read_json()['ciphers']):
        key_button = tk.Radiobutton(root, text=key['title'], font=(
            'Arial', 15), variable=selected_key_index, value=index, justify=tk.LEFT, command=submit_key)
        key_button.grid(row=(index + 1), column=1, ipady=7, sticky='nw')
    key_button.wait_variable(selected_key_index)


def encrypt_menu():
    main_menu()
    key_selector()
    title_widget = tk.Label(
        root,
        text='Type in some text that you want to encrypt: ',
        wraplength=200,
        font=('Arial', 15))
    text_entry = tk.Entry(root)

    def submit():
        title_widget = tk.Label(
            root,
            text='Your encrypted text: ',
            wraplength=200,
            font=('Arial', 15))

        encrypted_text = tk.Text(root, wrap=tk.CHAR, width=40)
        encrypted_text.insert(tk.END, encryption_tools.encrypt(
            text_entry.get(), cipher_tools.unsimplify_cipher(selected_key['cipher'])))

        encrypted_text.grid(row=4, column=2, sticky='w')
        title_widget.grid(row=3, column=2, sticky='w')
    submit_button = tk.Button(
        root, text="Done", font=('Arial', 20), command=submit)

    title_widget.grid(row=0, column=2, sticky='w')
    text_entry.grid(row=1, column=2, ipady=8, ipadx=22, sticky='w')
    submit_button.grid(row=2, column=2, ipadx=47, sticky='w')


def decrypt_menu():
    main_menu()
    key_selector()
    title_widget = tk.Label(
        root,
        text='Type in some text that you want to decrypt: ',
        wraplength=200,
        font=('Arial', 15))
    text_entry = tk.Entry(root)

    def submit():
        title_widget = tk.Label(
            root,
            text='Your decrypted text: ',
            wraplength=200,
            font=('Arial', 15))

        encrypted_text = tk.Text(root, wrap=tk.CHAR, width=40)
        encrypted_text.insert(tk.END, encryption_tools.decrypt(
            text_entry.get(), cipher_tools.unsimplify_cipher(selected_key['cipher'])))

        encrypted_text.grid(row=4, column=2, sticky='w')
        title_widget.grid(row=3, column=2, sticky='w')
    submit_button = tk.Button(
        root, text="Done", font=('Arial', 20), command=submit)

    title_widget.grid(row=0, column=2, sticky='w')
    text_entry.grid(row=1, column=2, ipady=8, ipadx=22, sticky='w')
    submit_button.grid(row=2, column=2, ipadx=47, sticky='w')


def list_keys():
    main_menu()
    title_widget = tk.Label(
        root,
        text='Your keys: ',
        wraplength=200,
        font=('Arial', 20))
    title_widget.grid(row=0, column=1, sticky='w')

    for index, key in enumerate(st.read_json()['ciphers']):
        listed_key = tk.Button(root, text=key['title'], font=(
            'Arial', 20), width=30, anchor='w')
        listed_key.grid(row=index + 1, column=1)


def main_menu():
    destroy_widgets()
    options = (("Encrypt", encrypt_menu), ("Decrypt", decrypt_menu),
               ("List Keys", list_keys), ("Make key", None), ('Delete Key', None))
    for button in options:
        menu_button = tk.Button(root, text=button[0], font=(
            'Arial', 20), width=10, command=button[1])
        if(options.index(button) != 0):
            menu_button.grid(row=options.index(button), padx=5, sticky='nw')
        else:
            menu_button.grid(row=options.index(button),
                             padx=5, pady=(5, 0), sticky='nw')


main_menu()
root.mainloop()
