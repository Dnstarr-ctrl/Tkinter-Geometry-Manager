from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry("400x500")
button=Button(text="Click me")
button.pack()

def event_handler(event):
    print(event.char)
window.bind("<Key>",event_handler)

def button_handler(event):
    print("Button is clicked")
button.bind("<Button-1>",button_handler)













window.mainloop()