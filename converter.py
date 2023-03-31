from tkinter import *
from class_convert import *

def send_data():
    data_from = list_from.get(ACTIVE)
    data_to = list_to.get(ACTIVE)
    value = int(En_from.get())
    obj = converter(data_from,data_to,value)

    En_to.delete(0,END)
    En_to.insert(END,obj.convert())


window = Tk()
window.title('Converter')
# window.geometry('270x260')
window.resizable(0,0)

my_font = ('Sitka Subheading Semibold',11)

Label(window,text='From',font=my_font).grid(row=0,column=0,sticky=W,padx=5)
En_from = Entry(window,font=my_font)
En_from.grid(row=1,column=0,sticky=W,padx=5,pady=2)

list_from = Listbox(window,font=my_font,exportselection=False)
list_from.grid(row=2,column=0,sticky=W,padx=5,pady=5)
list_from.insert(END,'Gram')
list_from.insert(END,'Kg')
list_from.insert(END,'Ton')


Label(window,text='To',font=my_font).grid(row=0,column=1,sticky=W,padx=5)
En_to = Entry(window,font=my_font)
En_to.grid(row=1,column=1,sticky=E,padx=5,pady=2)

list_to = Listbox(window,font=my_font,exportselection=False)
list_to.grid(row=2,column=1,sticky=E,padx=5,pady=5)
list_to.insert(END,'Gram')
list_to.insert(END,'Kg')
list_to.insert(END,'Ton')


btn = Button(window,text='Convert',command=send_data)
btn.grid(row=3,column=0,padx=5,pady=5,columnspan=2,sticky=W+E)

window.mainloop()
