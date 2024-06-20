import tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import string
import os

root = Tk()
# root.geometry('400x300')
root.resizable(False, False)
root.title('Generate Password For Apps')

values = ['Discord', 'Telegram', 'Instagram', 'Soft98.ir', 'Nobitex', 'Bazaar', 'BingX', 'Google', 'Codm',
          'Clash of Clans', 'Digikala', 'Divar', 'Gmail', 'Pinterest', 'Mobile.ir', '...']

values.sort()


def on_combobox_select(event):
    selected_value = combo_var.get()
    print(f'selected value: {selected_value}')
    if selected_value == '...':
        with open('otherapp.txt', 'w') as f:
            f.write('otherapp=True')
            f.close()
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

    context_menu = Menu(root, tearoff=0)
    context_menu.add_command(label='Copy', command=copy_to_clipboard)

    labelpass = Entry(root, state='readonly', readonlybackground='white', fg='black', font=('Calibri', 14),justify='center')
    var = StringVar()
    var.set('passw')
    labelpass.config(textvariable=var)
    labelpass.grid(row=1, column=1, columnspan=2, sticky=W + E, padx=8, pady=10)
    labelpass.bind('<Button-3>', show_context_menu)


def backToMainMenu():
    if os.path.exists('otherapp.txt'):
        os.remove('otherapp.txt')

    root.destroy()
    os.system('python main.py')


def savetodb():
    pass


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
