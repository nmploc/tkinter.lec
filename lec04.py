from tkinter import *

def submit():
    username=entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)

def clear():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window,
              font=('Arial',18),
              fg='#00FF00',
              bg='#000000',
              #show='*',
              )
entry.pack(side=LEFT)
#entry.insert(0,'Dumamay')

submit_button = Button(window,text="Submit",command=submit)
submit_button.pack(side=RIGHT)

clear_button = Button(window,text="Clear",command=clear)
clear_button.pack(side=LEFT)

backspace_button = Button(window,text="Backspace",command=backspace)
backspace_button.pack(side=LEFT)


window.mainloop()