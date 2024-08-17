from random import randint
import os

uspwd = input("Enter Your Password: ")
pwd = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
       "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
       "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

pw = ""
while pw != uspwd:
    pw = ""
    for letter in range(len(uspwd)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw += guess_pwd
    print(f"Trying: {pw}")
    print("Cracking Password....Please Wait....")
    os.system("cls")  # This clears the console on Windows. Remove or modify it if using another OS.

print("Your Password is:", pw)
