"""
This is a Book Shop manager app

Fields:
1. Title
2. Author
3. Year
4. ISBN

Actions:
1. View all records
2. Search an entry
3. Add entry
4. Update entry
5. Delete entry
6. Close

"""

from tkinter import *
import backend as be

def get_selected_row(event):  #event is a special variable
    global selected_tuple
    try:
        index=list1.curselection()[0]   #curselection returns a tuple with the index value
        selected_tuple = list1.get(index)
        #return selected_tuple
        title_entry.delete(0,END)
        title_entry.insert(END,selected_tuple[1])
        author_entry.delete(0,END)
        author_entry.insert(END,selected_tuple[2])
        year_entry.delete(0,END)
        year_entry.insert(END,selected_tuple[3])
        isbn_entry.delete(0,END)
        isbn_entry.insert(END,selected_tuple[4])
    except IndexError:
        pass


def view_command():
    # Populate list box
    list1.delete(0,END) #Deletes all records in a list box
    for row in be.viewall():
        list1.insert(END, row)


def search_command():
    list1.delete(0,END)
    for row in be.search(title.get(),author.get(),year.get(),isbn.get()):
        list1.insert(END, row)


def add_command():
    be.insert(title.get(),author.get(),year.get(),isbn.get())
    view_command()


def delete_command():
    #be.delete(get_selected_row()[0])
    be.delete(selected_tuple[0])

def update_command():
    be.update(selected_tuple[0],title.get(),author.get(),year.get(),isbn.get())

#user interface design
window = Tk()
window.wm_title("Book Shop")
#Title field
title_label = Label(window, text="Title")
title_label.grid(row=0,column=0)
title = StringVar()
title_entry = Entry(window, textvariable=title)
title_entry.grid(row=0,column=1)
#Filler
filler1_label = Label(window, text="   ")
filler1_label.grid(row=0,column=2)
#Author field
author_label = Label(window, text="Author")
author_label.grid(row=0,column=3)
author = StringVar()
author_entry = Entry(window, textvariable=author)
author_entry.grid(row=0,column=4)
#Filler
filler2_label = Label(window, text="   ")
filler2_label.grid(row=0,column=5)


#Year field
year_label = Label(window, text="Year")
year_label.grid(row=1,column=0)
year = StringVar()
year_entry = Entry(window, textvariable=year)
year_entry.grid(row=1,column=1)
#Filler
filler3_label = Label(window, text="   ")
filler3_label.grid(row=1,column=2)
#Author field
isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1,column=3)
isbn = StringVar()
isbn_entry = Entry(window, textvariable=isbn)
isbn_entry.grid(row=1,column=4)
#Filler
filler4_label = Label(window, text="   ")
filler4_label.grid(row=1,column=5)

list1 = Listbox(window, height=10, width = 35)
list1.grid(row=2,column=0,rowspan=10,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)  #Invoke the function when a row is selected

viewall_button = Button(window,text="View all",width=12,command=view_command)
viewall_button.grid(row=2,column=4)
search_button = Button(window,text="Search Entry",width=12,command=search_command)
search_button.grid(row=3,column=4)
addentry_button = Button(window,text="Add Entry",width=12,command=add_command)
addentry_button.grid(row=4,column=4)
update_button = Button(window,text="Update Entry",width=12,command=update_command)
update_button.grid(row=5,column=4)
delete_button = Button(window,text="Delete Entry",width=12,command=delete_command)
delete_button.grid(row=6,column=4)
close_button = Button(window,text="Close",width=12,command=window.destroy)
close_button.grid(row=7,column=4)




window.mainloop()