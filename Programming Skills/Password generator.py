#password Generator
import random
import string

password_length = int(input("Enter Password Length"))
letters = string.ascii_letters
digits = string.digits
spec_char = string.punctuation
Char = letters + digits + spec_char

pass_list = random.choices(Char,k=password_length)

password = ''.join(pass_list)

print(f'Password: {password}')

