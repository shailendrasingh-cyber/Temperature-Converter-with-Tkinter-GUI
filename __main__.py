from tkinter import *

w = Tk()
w.geometry("1200x675")  # Set the window size to 1000x500 pixels

var1 = DoubleVar()  # Celsius
var2 = DoubleVar()  # Fahrenheit

def temp_celsius_to_fahrenheit():
    label3.config(text="Fahrenheit: " + str(var1.get() * 1.8 + 32) + " °F")
    label3.place(x=350 , y =  340)

def temp_fahrenheit_to_celsius():
    label3.config(text="Celsius: " + str((var2.get() - 32) / 1.8) + " °C"  )
    label3.place(x=350 , y =  340)

f = Frame(w)
f.pack()


canvas = Canvas(w, width=1200, height=675)
canvas.pack()

background_image = PhotoImage(file="image.png")
canvas.create_image(0, 0, anchor=NW, image=background_image)

heading_text = "TEMPERATURE CONVERTER"
canvas.create_text(500, 50, text=heading_text, font=("Arial", 18), fill="black")



label1 = Label(w, text="Temperature in Celsius", font=("Arial", 18))
label1.place(x=200, y=100)

label2 = Label(w, text="Temperature in Fahrenheit", font=("Arial", 18))
label2.place(x=200, y=230)

E1 = Entry(w, font=("Arial", 18), textvariable=var1)
E1.place(x=500, y=100)

E2 = Entry(w, font=("Arial", 18), textvariable=var2)
E2.place(x=550, y=230)

label3 = Label(w, font=("Arial", 25))
label3.place(x=550, y=400)

B1 = Button(w, text="Convert to Fahrenheit", font=("Arial", 20), command=temp_celsius_to_fahrenheit)
B1.place(x=400, y=160)

B2 = Button(w, text="Convert to Celsius", font=("Arial", 20), command=temp_fahrenheit_to_celsius)
B2.place(x=400, y=280)

w.mainloop()
