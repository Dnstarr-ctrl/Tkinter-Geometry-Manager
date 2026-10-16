from tkinter import *
w=Tk()
w.title("Numberpad")
w.geometry("250x300")
frame=Frame(master=w, width=240, height=290 ,relief=SUNKEN, borderwidth=10, bg="black")
nums=[[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]
for i in range(4):
    w.columnconfigure(i, weight=1, minsize=75)
    w.rowconfigure(i, weight=1, minsize=75)
    for j in range(0,3):
        frame=Frame(master=w, relief=RIDGE, borderwidth=10, bg="black")
        frame.grid(row=i, column=j)
        lbl=Label(master=frame, text=nums[i][j])
        lbl.pack()
w.mainloop()