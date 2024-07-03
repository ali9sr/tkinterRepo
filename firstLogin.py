from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
import sqlite3

root = Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('New User')


def makeFile(name, email, phone):
    print(f'{name}\n{email}\n{phone}')
    with open('CONFIG.txt', 'w') as f:
        f.write(f'name={name}/email={email}/phone={phone}')
        f.close()
    conn = sqlite3.connect("Personal_Information.db")
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE if not exists Personal_Information(   
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Full_name VARCHAR(255) NOT NULL,
            Email VARCHAR(255) NOT NULL,
            Phone VARCHAR(255) NOT NULL
        )""")
        conn.commit()
        sql = 'INSERT INTO Personal_Information(Full_name, Email, Phone) VALUES (?, ?, ?)'
        c.execute(sql, (name, email, phone))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
    root.destroy()
    os.system('python main.py')


lable_name = ttk.Label(root, text='Name & Family:', bootstyle='inverse-primary')
entry_name = ttk.Entry(root, bootstyle='primary')

lable_Email = ttk.Label(root, text='Email:', bootstyle='inverse-primary')
entry_Email = ttk.Entry(root, bootstyle='primary')

lable_phone = ttk.Label(root, text='Phone Number:', bootstyle='inverse-primary')
entry_phone = ttk.Entry(root, bootstyle='primary')

button = ttk.Button(root, text='Submit',
                    command=lambda: makeFile(entry_name.get(), entry_Email.get(), entry_phone.get()), width=25)

lable_name.place(relx=0.5, rely=0.1, anchor=CENTER)
entry_name.place(relx=0.5, rely=0.2, anchor=CENTER)
lable_Email.place(relx=0.5, rely=0.3, anchor=CENTER)
entry_Email.place(relx=0.5, rely=0.4, anchor=CENTER)
lable_phone.place(relx=0.5, rely=0.5, anchor=CENTER)
entry_phone.place(relx=0.5, rely=0.6, anchor=CENTER)
button.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
