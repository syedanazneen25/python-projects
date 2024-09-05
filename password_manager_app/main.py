from tkinter import *
from tkinter import messagebox
import pyperclip 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letter = [random.choice(letters) for letter in range(random.randint(8, 10))]
    password_number = [random.choice(numbers) for number in range(random.randint(2, 4))]
    password_symbol = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password = password_letter + password_number + password_symbol
    random.shuffle(password)
    gen_password = ''.join(password)
    password_entry.insert(0, gen_password)
    pyperclip.copy(gen_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!!", message="Please don't leave empty fields.")
    else:
        save_data = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Email: {email}\n Password: {password}\n Is it okay to save?")
        if save_data:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200, highlightthickness=0)
pass_img = PhotoImage(file="password_manager_app/logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "syedanazneen@gmail.com")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
pass_gen = Button(text="Generate Password", command=gen_password)
pass_gen.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()