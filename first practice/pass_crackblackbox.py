import random
import string
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def crack_password(uspwd):
    pwd = string.ascii_lowercase + string.digits
    pw = ""
    while pw != uspwd:
        pw = "".join(random.choice(pwd) for _ in range(len(uspwd)))
        clear_screen()
        print("Cracking Password....Please Wait....")
        print("Current Guess:", pw)
    print("Your Password is:", pw)

uspwd = input("Enter Your Password: ")
crack_password(uspwd)