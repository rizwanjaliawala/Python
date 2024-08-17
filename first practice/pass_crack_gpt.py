from itertools import product
import string

def brute_force_crack(uspwd):
    chars = string.ascii_lowercase + string.digits  # "abcdefghijklmnopqrstuvwxyz0123456789"
    attempts = 0

    for length in range(1, len(uspwd) + 1):
        for guess in product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == uspwd:
                return guess, attempts

uspwd = input("Enter Your Password: ")
cracked_pwd, attempt_count = brute_force_crack(uspwd)
print(f"Your Password is: {cracked_pwd} (found in {attempt_count} attempts)")