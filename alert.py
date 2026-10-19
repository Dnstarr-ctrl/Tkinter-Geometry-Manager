from tkinter import *
from tkinter import messagebox
w=Tk()
w.geometry("400x500")
def msg():
    messagebox.showwarning("Alert!","TESTING ALERT FUNCTION")

button=Button(text="Resolve/Check for viruses",command=msg)
button.place(x=40,y=100)
w.mainloop()