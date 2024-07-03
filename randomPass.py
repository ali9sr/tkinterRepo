import tkinter
from tkinter import *
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import string
import os
from random import choices
import sqlite3

root = Tk()
# root.geometry('400x300')
root.resizable(False, False)
root.title('Generate Random Password')

# def getv(status_L, status_U, status_D, status_P):

checkboxv_L = tkinter.BooleanVar()
checkboxv_U = tkinter.BooleanVar()
checkboxv_D = tkinter.BooleanVar()
checkboxv_P = tkinter.BooleanVar()

global labelpasss


def backToMainMenu():
    root.destroy()
    os.system('python main.py')


def getv():
    pass


def pass_maker(length=8, uppercase=False, lowercase=False, digits=False, pun=False):
    p = ''

    if uppercase:
        p += string.ascii_uppercase

    if lowercase:
        p += string.ascii_lowercase

    if digits:
        p += string.digits

    if pun:
        p += string.punctuation

    # if p == '':
    #     p += string.ascii_letters

    try:
        return ''.join(choices(p, k=length))
    except:
        return 'hadagal yek option entekhab konid'


def GeneratePass():
    # print(f'Lower Case: {checkboxv_L.get()}')
    # print(f'Uppercase: {checkboxv_U.get()}')
    # print(f'Digits: {checkboxv_D.get()}')
    # print(f'Punctuation: {checkboxv_P.get()}')
    global labelpasss
    var = StringVar()
    uppercase = checkboxv_U.get()
    lowercase = checkboxv_L.get()
    digits = checkboxv_D.get()
    punc = checkboxv_P.get()

    try:
        length = int(lengthEntry.get())
        if 6 <= length <= 16:
            Length = length
        else:
            Length = 8
            print('adad pishfarz 8 ast va password ba 8 vagham sakhteh shod')
            print('adad motabar bein 6 ta 16 vared konid')
    except ValueError:
        Length = 8
        # print('adad pishfarz 8 ast va password ba 8 ragham sakhteh shod')
        # print('is not a number')

    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(labelpass.get())

    def show_context_menu(event):
        labelpass.select_range(0, tkinter.END)
        labelpass.icursor(tkinter.END)
        context_menu.post(event.x_root, event.y_root)

    context_menu = Menu(root, tearoff=0)
    context_menu.add_command(label='Copy', command=copy_to_clipboard)

    labelpass = Entry(root, state='readonly', readonlybackground='white', fg='black', font=('Calibri', 14),
                      justify='center')

    var.set(pass_maker(length=Length, uppercase=uppercase, lowercase=lowercase, digits=digits, pun=punc))
    labelpass.config(textvariable=var)
    labelpass.grid(row=1, column=1, columnspan=2, sticky=W + E, padx=8, pady=18, ipadx=8)
    labelpass.bind('<Button-3>', show_context_menu)
    labelpasss = labelpass.get()


def savetodb():
    global labelpasss
    print(labelpasss)
    conn = sqlite3.connect("Passwords.db")
    c = conn.cursor()
    section = "Random Password"
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


def on_click(event):
    lengthEntry.configure(state=NORMAL)
    lengthEntry.delete(0, END)
    lengthEntry.unbind('<Button-1>', on_click_id)


checkBoxLowercase = ttk.Checkbutton(root, bootstyle='primary', text='Lowercase', variable=checkboxv_L)
checkBoxUppercase = ttk.Checkbutton(root, bootstyle='primary', text='Uppercase', variable=checkboxv_U)
checkBoxDigit = ttk.Checkbutton(root, bootstyle='primary', text='Digits', variable=checkboxv_D)
checkBoxPunctuation = ttk.Checkbutton(root, bootstyle='primary', text='Special char', variable=checkboxv_P)

# checkBoxLowercase.state(['selected'])
# checkBoxUppercase.state(['selected'])

buttonGenerate = ttk.Button(root, text='Generate Password', command=lambda: GeneratePass())
buttonBackMain = ttk.Button(root, text='Back Main Menu', command=backToMainMenu)
buttonSaveToDb = ttk.Button(root, text='Save Password', command=savetodb)

lengthEntry = ttk.Entry(root, justify='center')
lengthEntry.insert(0, 'Pishfarz 8')
on_click_id = lengthEntry.bind('<Button-1>', on_click)
lengthLabel = ttk.Label(root, text='Password Length:', font=('Calibri', 12))

checkBoxLowercase.grid(row=2, column=1, sticky=W + E, padx=8)
checkBoxUppercase.grid(row=2, column=2, sticky=W + E, padx=6)
checkBoxDigit.grid(row=3, column=1, sticky=W + E, padx=8, pady=8)
checkBoxPunctuation.grid(row=3, column=2, sticky=W + E, pady=8, padx=6)

lengthEntry.grid(row=4, column=2, sticky=E, padx=8)
lengthLabel.grid(row=4, column=1, sticky=W, padx=8)

buttonGenerate.grid(row=5, column=1, padx=8, pady=10, sticky=W)
buttonSaveToDb.grid(row=5, column=2, padx=8, sticky=E)
buttonBackMain.grid(row=6, column=1, columnspan=2, sticky=W + E, padx=8, pady=8)

root.mainloop()
