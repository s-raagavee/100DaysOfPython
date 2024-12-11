#Task: Ask user how many letters, symbols and numbers they want in 
# their password and create a random password

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Version: Generate the password in sequence. Letters, then symbols, 
# then numbers.
'''
password = ""

#run a loop for each category and add to string

for letter in range(0, nr_letters):
    password += letters[random.randint(0, len(letters)-1)]

for symbol in range(0, nr_symbols):
    password += symbols[random.randint(0, len(symbols)-1)]

for number in range(0, nr_numbers):
    password += numbers[random.randint(0, len(numbers)-1)]

#print password
print(f"Your password is {password}")
'''


#Hard Version: n the advanced version of this project the final 
# password does not follow a pattern

password = []

#run a loop for each category and add to list

for letter in range(0, nr_letters):
    password.append(letters[random.randint(0, len(letters)-1)])

for symbol in range(0, nr_symbols):
    password.append(symbols[random.randint(0, len(symbols)-1)])

for number in range(0, nr_numbers):
    password.append(numbers[random.randint(0, len(numbers)-1)])

#randomly shuffle list
random.shuffle(password)

#print each character of the list into a single string
str_password = ""
for item in password:
    str_password += item

#print sring password
print(f"Your password is {str_password}")
