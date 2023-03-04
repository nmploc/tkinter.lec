"""in this library we use hex code with "#" to import color
"""

from tkinter import  *

window = Tk()
window.geometry("500x500") #size of the window

photo = PhotoImage(file='download.png')

window.config(background="#FDD36A")
#back ground color of the window

label = Label(window,
              text="Hello",#text in the label
              font=('Arial',40),#font and sixe of the text
              fg='#00FF00',#text color
              bg='Black',#background color
              relief=RAISED, #shade of the border
              bd=10,#border = x pixels
              padx=20,pady=20,#add pixels between text and border
              image=photo,#import image
              compound='bottom'#change position of the image
              )
label.pack()
#label.place(x=440,y=470)

window.mainloop()