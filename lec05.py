import tkinter as tk

def display():
    if(x.get()):
        print("You agree")
    else:
        print("You don't agrree")

window = tk.Tk()

x = tk.BooleanVar()
photo = tk.PhotoImage(file='download.png')

check_button= tk.Checkbutton(window,
                             text="I agree to something",
                             font=('Comic Sans',20),
                             fg='#00FF00',bg='#000000',activeforeground='#00FF00',activebackground='#000000',
                            variable=x,
                            onvalue=True,
                            offvalue=False,
                            command=display,padx=25,pady=10,
                            image=photo,
                            compound='left')
check_button.pack()

window.mainloop()