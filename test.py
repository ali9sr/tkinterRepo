import tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from tkinter import messagebox

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)


# add frames to notebook

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')

lab = Label(frame1,text='frame 1')
lab2 = Label(frame2,text='frame 2')
lab.grid()
lab.grid()


# w = Label(root, text ='GeeksForGeeks', font = "50")
# w.pack()
#
# messagebox.showinfo("showinfo", "Information")
#
# messagebox.showwarning("showwarning", "Warning")
#
# messagebox.showerror("showerror", "Error")
#
# messagebox.askquestion("askquestion", "Are you sure?")
#
# messagebox.askokcancel("askokcancel", "Want to continue?")
#
# messagebox.askyesno("askyesno", "Find the value?")
#
#
# messagebox.askretrycancel("askretrycancel", "Try again?")

root.mainloop()
