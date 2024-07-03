import tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sqlite3
from cryptography.fernet import Fernet
import os


def fetch_passwords(section):
    conn = sqlite3.connect("Passwords.db")
    c = conn.cursor()
    try:
        c.execute("""SELECT Password FROM Passwords WHERE Section = ?""", (section,))
        passwords = c.fetchall()
        return [p[0] for p in passwords]
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()


def update_password_list(event):
    selected_section = section_var.get()
    passwords = fetch_passwords(selected_section)
    password_list.delete(0, END)
    for password in passwords:
        password_list.insert(END, password)


def backToMainMenu():
    root.destroy()
    os.system('python main.py')


root = Tk()
root.geometry('400x300')
root.resizable(False, False)
root.title('Saved Passwords')

section_var = StringVar()
sections = ["Random Password", "Personal Password", "App Generation Password"]
section_menu = ttk.Combobox(root, textvariable=section_var, values=sections)
section_menu.current(0)
buttonBackMain = ttk.Button(root, text='Back Main Menu', command=backToMainMenu)
section_menu.place(relx=0.5, rely=0.1, anchor=CENTER)
section_menu.bind("<<ComboboxSelected>>", update_password_list)
buttonBackMain.grid(row=6, column=1, columnspan=2, sticky=W + E, padx=8, pady=8)

password_list = Listbox(root, width=50, height=10)
password_list.place(relx=0.5, rely=0.45, anchor=CENTER)
buttonBackMain.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
