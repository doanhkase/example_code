from tkinter import *

window = Tk()
window.title("kase")
window.geometry('350x200')

def clicked():
    lbl.configure(text="Button was clicked !!")

lbl = Label(window, 
            text="Hello", 
            font=("Arial Bold", 14))
lbl.grid(column=0, row=0)

# btn = Button(window, text="Click Me")
btn = Button(window, text= "Click Me", command=clicked)
btn.grid(column=1, row=1)

window.mainloop()
