import tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import string
import os
import sqlite3
from tkinter import messagebox

root = Tk()
# root.geometry('400x300')
root.resizable(False, False)
root.title('Generate Password For Apps')

values = ['Discord', 'Telegram', 'Instagram', 'Soft98.ir', 'Nobitex', 'Bazaar', 'BingX', 'Google', 'Codm',
          'Clash of Clans', 'Digikala', 'Divar', 'Gmail', 'Pinterest', 'Mobile.ir', '...']

values.sort()
labelpasss = None

with open('CONFIG.txt', 'r') as f:
    data = f.read().split('/')
    name = data[0].split('=')[1]
    email = data[1].split('=')[1]
    phone = data[2].split('=')[1]

edittext = ttk.Entry(root, justify='center')


def on_combobox_select(event):
    def on_click(event):
        edittext.configure(state=NORMAL)
        edittext.delete(0, END)
        edittext.unbind('<Button-1>', on_click_id)

    selected_value = combo_var.get()
    print(f'selected value: {selected_value}')
    if selected_value == '...':
        with open('otherapp.txt', 'w') as f:
            f.write('otherapp=True')
            f.close()
        edittext.delete(0, END)
        edittext.insert(0, 'Name Your App:')
        on_click_id = edittext.bind('<Button-1>', on_click)
        edittext.grid(row=3, column=1, columnspan=2, sticky=W + E, padx=8, pady=8)

    elif not selected_value == '...':
        with open('otherapp.txt', 'w') as f:
            f.write('otherapp=False')
            f.close()


def GeneratePass():
    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(labelpass.get())

    def show_context_menu(event):
        labelpass.select_range(0, tkinter.END)
        labelpass.icursor(tkinter.END)
        context_menu.post(event.x_root, event.y_root)

    global labelpasss
    context_menu = Menu(root, tearoff=0)
    context_menu.add_command(label='Copy', command=copy_to_clipboard)

    labelpass = Entry(root, state='readonly', readonlybackground='white', fg='black', font=('Calibri', 14),
                      justify='center')

    namermk1 = name.split(' ')[0].capitalize()
    namermk2 = name.split(' ')[1].capitalize()
    phonermk = phone[:4]

    otherapp = edittext.get()
    var = StringVar()
    if not combo_var.get() == '...':
        var.set(f'{namermk2}{phonermk}{combo_var.get()}#')
        labelpass.config(textvariable=var)
        labelpass.grid(row=1, column=1, columnspan=2, sticky=W + E, padx=8, pady=10)
        labelpass.bind('<Button-3>', show_context_menu)
        labelpasss = labelpass.get()
    elif combo_var.get() == '...' and otherapp.isalpha():
        if not otherapp == '':
            if not otherapp == 'Name Your App:':
                var.set(f'{namermk2}{phonermk}{otherapp}#')
                labelpass.config(textvariable=var)
                labelpass.grid(row=1, column=1, columnspan=2, sticky=W + E, padx=8, pady=10)
                labelpass.bind('<Button-3>', show_context_menu)
                labelpasss = labelpass.get()
            elif otherapp == 'Name Your App:':
                messagebox.showerror("Error", "lotfan barname khod ra entekhab konid-88")
        elif otherapp == '':
            messagebox.showerror("Error", "lotfan barname khod ra entekhab konid-90")
    else:
        messagebox.showerror("Error", "lotfan barname khod ra entekhab konid-94")

def backToMainMenu():
    if os.path.exists('otherapp.txt'):
        os.remove('otherapp.txt')

    root.destroy()
    os.system('python main.py')


def savetodb():
    global labelpasss
    # print(labelpasss)
    conn = sqlite3.connect("Passwords.db")
    c = conn.cursor()
    section = "App Generation Password"
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
        # print(f"Error: {e}")
        messagebox.showerror("Error", "lotfan barname khod ra type karde va roye generate click konid")
    finally:
        conn.close()


combo_var = tkinter.StringVar()

combo_box = ttk.Combobox(root, textvariable=combo_var)
combo_box['values'] = values
combo_box.current(9)

labelHint = ttk.Label(root, text='Choose Your Apps:', font=('Calibri', 14))
buttonGenerate = ttk.Button(root, text='Generate Password', command=GeneratePass)
buttonBackMain = ttk.Button(root, text='Back Main Menu', command=backToMainMenu)
buttonSaveToDb = ttk.Button(root, text='Save Password', command=savetodb)

buttonGenerate.grid(row=4, column=1, padx=8, sticky=W + E, columnspan=2)
buttonSaveToDb.grid(row=5, column=1, padx=8, pady=4, sticky=W + E, columnspan=2)
buttonBackMain.grid(row=6, column=1, sticky=W + E, padx=8, pady=10, columnspan=2)
labelHint.grid(row=2, column=1, sticky=W, padx=8)
combo_box.grid(row=2, column=2, sticky=E, padx=8, pady=8)

combo_box.bind("<<ComboboxSelected>>", on_combobox_select)

root.mainloop()
