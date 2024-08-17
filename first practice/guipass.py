import tkinter as tk
from tkinter import messagebox
import itertools
import string
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def crack_password(uspwd):
    pwd = string.ascii_lowercase + string.digits
    for attempt in itertools.product(pwd, repeat=len(uspwd)):
        pw = "".join(attempt)
        print("Current Guess:", pw)
        if pw == uspwd:
            return pw

def start_cracking():
    uspwd = password_entry.get()
    if uspwd:
        result = crack_password(uspwd)
        if result:
            messagebox.showinfo("Password Cracked", f"Your password is: {result}")
        else:
            messagebox.showinfo("Password Not Cracked", "Unable to crack password")
    else:
        messagebox.showerror("Error", "Please enter a password")

root = tk.Tk()
root.title("Password Cracker")

password_label = tk.Label(root, text="Enter Your Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*", width=20)
password_entry.pack()

crack_button = tk.Button(root, text="Crack Password", command=start_cracking)
crack_button.pack()

root.mainloop()