import tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os

root = Tk()
root.geometry('400x300')
root.resizable(False, False)
root.title('Generate Personal Password')

with open('CONFIG.txt', 'r') as f:
    data = f.read().split('/')
    name = data[0].split('=')[1]
    email = data[1].split('=')[1]
    phone = data[2].split('=')[1]


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

    if mode == 1:
        phoneRemake = phone[:7]
        phone2Remake = phone[7:]
        nameRemake = name.split(' ')[0]
        familyRemake = name.split(' ')[1]
        passw = f"{phoneRemake}{nameRemake}{phone2Remake}{familyRemake}@"
        labelpass = Entry(root, state='readonly', readonlybackground='white', fg='black', font=('Calibri', 14),justify='center')
        var = StringVar()
        var.set(passw)
        labelpass.config(textvariable=var)
        labelpass.place(relx=0.5, rely=0.2, anchor=CENTER)
        labelpass.bind('<Button-3>', show_context_menu)
    elif mode == 2:
        nameRemake2 = name.split(' ')[0]
        passw = f'{phone}{nameRemake2}#'
        labelpass = Entry(root, state='readonly', readonlybackground='white', fg='black', font=('Calibri', 14),justify='center')
        var = StringVar()
        var.set(passw)
        labelpass.config(textvariable=var)
        labelpass.place(relx=0.5, rely=0.2, anchor=CENTER)
        labelpass.bind('<Button-3>', show_context_menu)
        labelpass.bind('<Button-1>', show_context_menu)


def backMainPage():
    root.destroy()
    os.system('python main.py')


def savetodb():
    pass


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
