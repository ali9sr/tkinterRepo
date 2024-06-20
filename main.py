from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os

root = Tk()

root.title('Password Generator Plus')

# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# root.geometry(f'{width}x{height}')
# root.state('zoomed')

root.geometry('400x300')
root.resizable(False, False)
# root.overrideredirect(True)


def changeThemeToLight():
    style = ttk.Style("cosmo")


def changeThemeToDark():
    style = ttk.Style('darkly')


def gotoGPP():  # generate personal password form
    root.destroy()
    os.system('python personalPass.py')


def gotoGRP():  # generate random password
    root.destroy()
    os.system('python randomPass.py')


def gotoGPFA():  # generate password for apps
    root.destroy()
    os.system('python generateForApp.py')


def gotoSP():  # saved password
    root.destroy()
    os.system('python savedPass.py')


button1 = ttk.Button(root, text='Generate Random Password', bootstyle=PRIMARY, command=gotoGRP)
button2 = ttk.Button(root, text='Generate Personal Password', bootstyle=PRIMARY, command=gotoGPP)
button3 = ttk.Button(root, text='Generate Password For App', bootstyle=PRIMARY, command=gotoGPFA)
button4 = ttk.Button(root, text='Saved Passwords', bootstyle=PRIMARY, command=gotoSP)

button1.place(relx=0.5, rely=0.3, anchor=CENTER)
button2.place(relx=0.5, rely=0.4, anchor=CENTER)
button3.place(relx=0.5, rely=0.5, anchor=CENTER)
button4.place(relx=0.5, rely=0.6, anchor=CENTER)

if not os.path.exists('CONFIG.txt'):
    print('you are a new user')
    os.system('python firstLogin.py')
    root.destroy()

root.mainloop()
