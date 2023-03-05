from tkinter import *

food=["Rice","Fish","Beef",0]

def order():
    if(x.get()==0):
        print("Rice")
    elif(x.get()==1):
        print("Fish")
    elif(x.get()==2):
        print("Beef")
    else:
        print("Huh ?? ")
window = Tk()

x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[i],
                              variable=x,
                              value=i,
                              padx=25,pady=25,
                              font=('Arial',15),
                              indicatoron=0,
                              width=25,
                              command=order)
    radiobutton.pack(anchor=W)

window.mainloop()