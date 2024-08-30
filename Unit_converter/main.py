from tkinter import *

def calculate():
    user_input = float(input.get())
    conversion_type = conversion_var.get()

    if conversion_type == "Miles to Km":
        result = round((user_input * 1.60934), 2)
        label_4.config(text=f"{result} Km")
    elif conversion_type == "Km to Miles":
        result = round((user_input / 1.60934), 2)
        label_4.config(text=f"{result} Miles")
    elif conversion_type == "Pounds to Kg":
        result = round((user_input * 0.453592), 2)
        label_4.config(text=f"{result} Kg")
    elif conversion_type == "Kg to Pounds":
        result = round((user_input / 0.453592), 2)
        label_4.config(text=f"{result} Pounds")

# Window setup
window = Tk()
window.title("Unit Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# Dropdown menu for conversion types
conversion_var = StringVar(value="Miles to Km")
conversion_menu = OptionMenu(window, conversion_var, "Miles to Km", "Km to Miles", "Pounds to Kg", "Kg to Pounds")
conversion_menu.config(width=15)
conversion_menu.grid(padx=10, pady=10, row=0, column=0)

# Input field
input = Entry()
input.config(width=10)
input.grid(padx=10, pady=10, row=0, column=1)

# Label for "is equal to"
label_3 = Label()
label_3.config(text="is equal to", font=("Courier", 15))
label_3.grid(padx=10, pady=10, row=1, column=0)

# Label to display the result
label_4 = Label()
label_4.config(text="0", font=("Courier", 15))
label_4.grid(padx=10, pady=10, row=1, column=1)

# Button to calculate the result
button = Button(command=calculate)
button.config(text="Calculate", font=("Courier", 10))
button.grid(padx=10, pady=10, row=2, column=1)

window.mainloop()
