from tkinter import *
from tkinter import messagebox
import random
import pyperclip as clip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyz")
    numbers = list("0123456789")
    symbols = list("!@#$%^&*?")

    # Password requirements
    password_chars = []
    password_chars.append(random.choice([ch.upper() for ch in letters]))  # 1 uppercase
    password_chars.extend(random.sample(numbers, 2))  # 2 digits
    password_chars.extend(random.sample(symbols, 2))  # 2 special chars
    password_chars.extend(random.sample(letters, 5))  # remaining lowercase to make 10 chars

    random.shuffle(password_chars)
    password = "".join(password_chars)
    clip.copy(password)

    # Update entry
    en3.delete(0, END)
    en3.insert(0, password)


    # Confirmation popup
    messagebox.showinfo("Password Generated", f"Password copied to clipboard:\n\n{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = en1.get()
    email = en2.get()
    password = en3.get()

    if not website or not email or not password:
        messagebox.showwarning("Oops!", "Please don't leave any fields empty!")
        return

    # Save to file
    with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")

    # Confirmation popup
    messagebox.showinfo("Saved", "Your credentials have been saved successfully!")

    # Clear fields
    en1.delete(0, END)
    en3.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
BG = "#f0f0f0"
window = Tk()
window.config(padx=40, pady=40, bg=BG)
window.title("My Password Manager")

# Canvas for logo
canv = Canvas(window, width=200, height=200, bg=BG, highlightthickness=0)
img = PhotoImage(file="logo.png")
canv.create_image(100, 100, image=img)
canv.grid(row=0, column=1)

# Label + Entry for Website
lb1 = Label(text="Website:", font=('Courier', 12, "bold"), fg="black", bg=BG)
lb1.grid(row=1, column=0, pady=5)
en1 = Entry(window, width=35)
en1.grid(row=1, column=1, columnspan=2, sticky="w", pady=5)

# Label + Entry for Email
lb2 = Label(text="Email/Username:", font=('Courier', 12, "bold"), fg="black", bg=BG)
lb2.grid(row=2, column=0, pady=5)
en2 = Entry(window, width=35)
en2.grid(row=2, column=1, columnspan=2, sticky="w", pady=5)
en2.insert(0, "your_email@example.com")  # Default email

# Label + Entry for Password
lb3 = Label(text="Password:", font=('Courier', 12, "bold"), fg="black", bg=BG)
lb3.grid(row=3, column=0, pady=5)
en3 = Entry(window, width=21)
en3.grid(row=3, column=1, pady=5)

# Generate Password Button
but1 = Button(text="Generate", command=generate_password, width=15, bg="#4CAF50", fg="white")
but1.grid(row=3, column=2, pady=5)

# Add Button (to save password)
but2 = Button(text="Add", width=36, command=save_password, bg="#2196F3", fg="white")
but2.grid(row=4, column=1, columnspan=2, pady=15)

window.mainloop()
