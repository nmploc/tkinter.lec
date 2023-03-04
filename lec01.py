import tkinter as tk
from tkinter import  *

window = tk.Tk()

window.title("Hello")

window.config(background="#FFA3FD")


label = tk.Label(window, text = "hola", font=('Roboto', 18))
label.pack(padx = 20, pady = 20)

textbox = tk.Text(window, font=('Arial ',18), height=1)
textbox.pack(pady = 20)

textbox1 = tk.Text(window, font=('Arial ',18), height=1)
textbox1.pack(pady = 10)

button = tk.Button(window, text="Show Message", font=('Arial', 18))
button.pack()

window.mainloop()

