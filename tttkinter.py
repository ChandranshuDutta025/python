from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Simple tkinter App")
frm = ttk.Frame(root,padding=5)
frm.grid()
ttk.Label(frm,text=" ").grid(column=0,row=0,padx=10,pady=10) 
ttk.Button(frm,text="Quit",command=root.destroy).grid(column=7,row=1)
root.mainloop()
