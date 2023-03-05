from tkinter import *

count = 0

def click():
    global count
    count+=1
    print(count)

window = Tk()

button = Button(window,
                text='click me',
                command=click,
                font=('Comic sans',30),
                fg="#00FF00",
                bg="#000000",
                activeforeground="blue",
                activebackground="black",
                )
button.pack()

window.mainloop()