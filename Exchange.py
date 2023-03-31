from tkinter import *

import requests

global_test = requests.get('https://api.coinlore.net/api/tickers/')
x = global_test.json()
# print(x['data'])
symbol = dict()

for i in x['data']:
    symbol[i['symbol']] = i['price_usd']

all_symbol = list(symbol.keys())

def price(e):
    data_from = list_form.get(ACTIVE)
    price_entry.delete(0,END)
    price_entry.insert(END,f'{symbol[data_from]} $')


def rial(e):
    data_from = list_form.get(ACTIVE)
    price_entry.delete(0,END)
    price_entry.insert(END,f'{float(symbol[data_from]) * float(usd_sell)} Rial')




def update(data):
    list_form.delete(0,END)
    for i in data:
        list_form.insert(END,i)

def symbolout(e):
    searching.delete(0,END)
    searching.insert(0,list_form.get(ACTIVE))

def check_symbol(e):
    typed = searching.get()
    if typed == '':
        data = all_symbol
    else:
        data =[]
        for i in all_symbol:
            if typed.lower() in i.lower():
                data.append(i)
    update(data)



usd = requests.get('http://api.navasan.tech/latest?api_key=freeNksAVbdGDtZXDxQGVHsC4Z44qXd5')
usd_sell = usd.json()
usd_sell = usd_sell['usd_sell']['value']

# print(usd_sell)

window = Tk()
window.title('Exchange')
# window.geometry('500x500')
window.resizable(0,0)
my_font = ('Sitka Subheading Semibold',11)

Label(window,text='Search Bar',font=my_font).pack(fill='both',expand=True,padx=5,pady=5)

searching = Entry(window,font=my_font)
searching.pack(fill='both',expand=True,padx=5,pady=5)
searching.bind('<KeyRelease>',check_symbol)

list_form = Listbox(window,font=my_font,exportselection=False)
list_form.pack(fill='both',expand=True,padx=5,pady=5)
update(all_symbol)
list_form.bind('<<ListboxSelect>>',symbolout)

btn = Button(window,text='Get The Price',font=my_font)
btn.pack(fill='both',expand=True,padx=5,pady=5)
btn.bind('<ButtonPress-1>',price)
btn.bind('<ButtonPress-3>',rial)

Label(window,text='Price',font=my_font).pack(fill='both',expand=True,padx=5,pady=5)

price_entry = Entry(window,font=my_font)
price_entry.pack(fill='both',expand=True,padx=5,pady=5)



window.mainloop()