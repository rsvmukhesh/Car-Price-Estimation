import tkinter

# --------------Function---------------#

def estimate():

    weights
    Fuel_W = -50771.6043
    km_w = -100754.823
    seller_w = -30109.3344
    year_w = 34142.33400
    owner_w = -4536.3964
    transmssion_w = -187004.29857

    y = (Fuel_W * int(fuel_entry.get())) + (km_w * int(km_entry.get())) + (seller_w * int(seller_entry.get()))
    y_1 = (year_w * int(year_entry.get())) + (owner_w * int(owner_entry.get())) + (transmssion_w * int(transmssion_w.get()))
    out = abs(y + y_1)

    canvas.itemconfig(note, fill='darkblue', text=f'The Estimated Price:{out}')

# -----------UI Setup---------------------#
window = tkinter.Tk()
window.title("Multiple linear Regression")
window.config(padx=50, pady=50)


# canvas

canvas = tkinter.Canvas(width=400, height=200, highlightthickness=0)
logo = tkinter.PhotoImage(file='cars.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=2, columnspan=2)
output = canvas.create_text(140, 180, text='The Estimate Price: 62000012.5', font=('Courier', 10,'bold'))

# labels

title = tkinter.Label(text='Car Price Estimation', font=('Courier', 15,'bold'), fg='#F37553')
title.grid(column=0, row=0, columnspan=3)

name = tkinter.Label(text='Car Name/Brand:', font=('Courier', 10))
name.grid(column=0, row=3)

Year = tkinter.Label(text='Year:', font=('Courier', 10))
Year.grid(column=0, row=4)

km_driven = tkinter.Label(text='km_driven:', font=('Courier', 10))
km_driven.grid(column=0, row=5)

fuel = tkinter.Label(text='Fuel:', font=('Courier', 10))
fuel.grid(column=0, row=6)

transmssion = tkinter.Label(text='Transmission:', font=('Courier',10))
transmssion.grid(column=0,row=9)

seller_type = tkinter.Label(text='Seller Type:', font=('Courier',10))
seller_type.grid(column=0, row=7)

note = tkinter.Label(text='Note: Fill the required details as mentioned below\n\n'
                          '1.Fuel: 0-CNG,1 - Diesel, 2- Electric, 3-LPG, 4-Petrol\n'
                          '2.Seller Type: 0-Dealer, 1-Individual, 2-Trustmark Dealer\n'
                          '3.Transmission: 1-Manual, 0-Automatic\n'
                          '4.Owner: 0-First owner, 2-second owner, 4-Third Owner \n '
                          '3-Test Drive Car, 1-Fourth & Above Car', font=('Arial Bold',10))
note.grid(column=0, row=12, columnspan=3)

owner = tkinter.Label(text='Owner:', font=('Courier',10))
owner.grid(column=0, row=8)

# Entrys

name_entry = tkinter.Entry(width=39)
name_entry.grid(column=1, row=3)

year_entry = tkinter.Entry(width=39)
year_entry.grid(column=1, row=4)

km_entry = tkinter.Entry(width=39)
km_entry.grid(column=1, row=5)

fuel_entry = tkinter.Entry(width=39)
fuel_entry.grid(column=1, row=6)

seller_entry = tkinter.Entry(width=39)
seller_entry.grid(column=1, row=7)

owner_entry = tkinter.Entry(width=39)
owner_entry.grid(column=1, row=8)

transmssion_entry = tkinter.Entry(width=39)
transmssion_entry.grid(column=1, row=9)
# Buttons

estimate = tkinter.Button(text='Estimate', command=estimate(), height=1, width=12)
estimate.grid(column=1, row=10)



window.mainloop()