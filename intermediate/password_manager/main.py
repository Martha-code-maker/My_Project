from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = Email_User_entry.get()
    pw = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pw
        }
    }
    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------FIND PASSWORD----------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="warning", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            pw = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Website: {email}\nPassword: {pw} ")
        else:
            messagebox.showinfo(title="warning", message="No details for the website exist.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

Email_User_label = Label(text="Email/Username:")
Email_User_label.grid(column=0, row=2)

Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)

website_entry = Entry(width=29)
website_entry.grid(column=1, row=1)

Email_User_entry = Entry(width=45)
Email_User_entry.grid(column=1, row=2, columnspan=2)
Email_User_entry.insert(0, "uj5253@gmail.com")

password_entry = Entry(width=29)
password_entry.grid(column=1, row=3)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
