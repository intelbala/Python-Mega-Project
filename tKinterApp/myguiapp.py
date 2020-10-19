from tkinter import *

window = Tk()

def convert_units():
    if e1_value.get() == "":
        print("Enter a valid unit in kgs")
    else:
        unit_kg = float(e1_value.get())
        unit_gms = unit_kg * 1000
        unit_lbs = unit_kg * 2.20462
        unit_oz = unit_kg * 35.274
        e2.delete(0,END)
        e2.insert(0,unit_gms)
        e3.delete(0,END)
        e3.insert(0,unit_lbs)
        e4.delete(0,END)
        e4.insert(0,unit_oz)

l1 = Label(window,text="Enter units in Kgs")
l1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1 = Button(window,text="Convert",command=convert_units)
b1.grid(row=0,column=2)


l2 = Label(window,text="Gms")
l2.grid(row=1,column=0)
e2 = Entry(window)
e2.grid(row=2,column=0)

l3 = Label(window,text="Lbs")
l3.grid(row=1,column=1)
e3 = Entry(window)
e3.grid(row=2,column=1)

l4 = Label(window,text="Oz")
l4.grid(row=1,column=2)
e4 = Entry(window)
e4.grid(row=2,column=2)

window.mainloop()