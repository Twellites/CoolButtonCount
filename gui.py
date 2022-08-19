from tkinter import *

count = 0

def click():
    global count 
    count+=1
    print(count)

window = Tk()



button = Button(window,
text="Click Me!",
command=click,
font=("JetBrains Mono", 30),
fg="#00FF00",
bg="black",
activeforeground="#00FF00",
activebackground="black",
state=ACTIVE,
compound='top')

button.pack()

window.mainloop()

