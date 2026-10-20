from tkinter import *
from tkinter import messagebox
w=Tk()
w.title("After School Routine Checker")
w.geometry("400x320")

heading=Label(w,text="My after school routine",font=("Arial",16,"bold"))
heading.pack(pady=10)

instruction=Label(w,text="Enter your after school routine task:")
instruction.pack()

task_entry=Entry(w,width=35)
task_entry.pack(pady=8)

def handle_click(event):
    """Update the message when the routine area is clicked."""
    routine_message.config(text="Routine area clicked!")

routine_message=Label(w,text="Click here to check your routine",bg="#d0efff",width=32,height=3)
routine_message.pack(pady=10)
routine_message.bind("<Button-1>",handle_click)

def check_routine():
    """Display the task or show a warning when it ismissing."""
    task = task_entry.get()
    if task=="":
        messagebox.showwarning("Missing Task","Please enter an after-school task.")
    else:
        routine_message.config(text="Next task: " + task)

check_button=Button(w,text="Check My Routine",command=check_routine)
check_button.pack(pady=10)

w.mainloop()