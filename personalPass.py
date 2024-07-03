import tkinter
from tkinter import *
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
import sqlite3
import hashlib
from cryptography.fernet import Fernet

root = Tk()
root.geometry('400x300')
root.resizable(False, False)
root.title('Generate Personal Password')

with open('CONFIG.txt', 'r') as f:
    data = f.read().split('/')
    name = data[0].split('=')[1]
    email = data[1].split('=')[1]
    phone = data[2].split('=')[1]

labelpasss = None


def generatePass(name, phone, mode):
    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(labelpass.get())

    def show_context_menu(event):
        labelpass.select_range(0, tkinter.END)
        labelpass.icursor(tkinter.END)
        context_menu.post(event.x_root, event.y_root)

    context_menu = Menu(root, tearoff=0)
    context_menu.add_command(label='Copy', command=copy_to_clipboard)
    global labelpasss
    if mode == 1:
        phoneRemake = phone[:7]
        phone2Remake = phone[7:]
        nameRemake = name.split(' ')[0].capitalize()
        familyRemake = name.split(' ')[1]
        passw = f"{phoneRemake}{nameRemake}{phone2Remake}{familyRemake}@"
        labelpass = Entry(root, state='readonly', readonlybackground='white', fg='black', font=('Calibri', 14),
                          justify='center')
        var = StringVar()
        var.set(passw)
        labelpass.config(textvariable=var)
        labelpass.place(relx=0.5, rely=0.2, anchor=CENTER)
        labelpass.bind('<Button-3>', show_context_menu)
        labelpasss = labelpass.get()
    elif mode == 2:
        nameRemake2 = name.split(' ')[0].capitalize()
        passw = f'{phone}{nameRemake2}#'
        labelpass = Entry(root, state='readonly', readonlybackground='white', fg='black', font=('Calibri', 14),
                          justify='center')
        var = StringVar()
        var.set(passw)
        labelpass.config(textvariable=var)
        labelpass.place(relx=0.5, rely=0.2, anchor=CENTER)
        labelpass.bind('<Button-3>', show_context_menu)
        labelpass.bind('<Button-1>', show_context_menu)
        labelpasss = labelpass.get()


def backMainPage():
    root.destroy()
    os.system('python main.py')


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def savetodb():
    global labelpasss
    hashed_password = encrypt_password(labelpasss)
    print(labelpasss)
    print(hashed_password)
    conn = sqlite3.connect("Passwords.db")
    c = conn.cursor()
    section = "Personal Password"
    try:
        c.execute("""CREATE TABLE if not exists Passwords(   
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Password VARCHAR(255) NOT NULL,
            Section VARCHAR(255) NOT NULL
        )""")
        conn.commit()
        sql = 'INSERT INTO Passwords(Password, Section) VALUES (?, ?)'
        c.execute(sql, (labelpasss, section))
        conn.commit()
        messagebox.showinfo('save to database', 'ba movafaghiat zakhire shod')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
    # get_password_from_db()


def load_key():
    return open('secret.key', 'rb').read()


key = load_key()
cipher_suite = Fernet(key)

cipher_suite = Fernet(key)


def encrypt_password(password):
    return cipher_suite.encrypt(password.encode()).decode()


# def decrypt_password(encrypted_password):
#     return cipher_suite.decrypt(encrypted_password.encode()).decode()


# def get_password_from_db():
#     conn = sqlite3.connect("Passwords.db")
#     c = conn.cursor()
#     try:
#         c.execute("SELECT Password FROM Passwords WHERE Section = ?", ("Personal Password",))
#         encrypted_password = c.fetchone()[0]
#         decrypted_password = decrypt_password(encrypted_password)
#         print(f"Decrypted password: {decrypted_password}")
#         return decrypted_password
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         conn.close()

# def test1():
#     print(radVar.get())


radVar = IntVar()

button = ttk.Button(root, text='Generate', command=lambda: generatePass(name, phone, radVar.get()), width=25)
button2 = ttk.Button(root, text='Back Main Menu', command=backMainPage, width=25)
button3 = ttk.Button(root, text='Save Password', command=savetodb, width=25)
radioBtnOne = ttk.Radiobutton(root, bootstyle='primary', text='Mode #1', variable=radVar, value=1)
radioBtnTwo = ttk.Radiobutton(root, bootstyle='primary', text='Mode #2', variable=radVar, value=2)

radioBtnOne.place(relx=0.4, rely=0.3, anchor=CENTER)
radioBtnTwo.place(relx=0.6, rely=0.3, anchor=CENTER)
button.place(relx=0.5, rely=0.4, anchor=CENTER)
button3.place(relx=0.5, rely=0.5, anchor=CENTER)
button2.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
