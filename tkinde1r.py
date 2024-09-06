from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Weather Forecast App")
frm = ttk.Frame(root)
frm.grid(padx=100, pady=200)
ttk.Label(frm,text="Your Location").grid(column=0,row=0,padx=10,pady=10)

root.mainloop()