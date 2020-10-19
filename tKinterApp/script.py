from tkinter import * #tkinter comes by default with Python 3. 

""" 
Tkinter GUI is made of of 2 components
1. Window
2. Widgets
"""

window = Tk()

def km_to_miles():
    # print(e1_value.get())
    miles = float(e1_value.get()) * 1.606
    t1.insert(END,miles)

b1=Button(window, text="Execute",command=km_to_miles)   #Command button
b1.grid(row=0,column=0)

e1_value = StringVar()

e1 = Entry(window,textvariable=e1_value)                  #Text entry
e1.grid(row=0,column=1)


t1 = Text(window,height=1,width=20) #multiline text box
t1.grid(row=0,column=3)




window.mainloop()