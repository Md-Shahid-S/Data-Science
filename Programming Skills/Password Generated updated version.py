import string
import random

pass_len = int(input("Enter the Length of password"))

include_letters = input('include letter? (y/n').lower() == 'y'
include_numbers = input('include numbers? (y/n').lower() == 'y'
include_special_char = input('include special char? (y/n').lower() == 'y'

password = ''
if include_letters:
    password += string.ascii_letters
if include_numbers:
    password += string.digits
if include_special_char:
    password += string.punctuation

if not password:
    print("Error: Select at least one char type")
else:
    print(''.join(random.choices(f"Password: {password}",k=pass_len)))
