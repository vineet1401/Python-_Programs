# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []
for i in range(nr_letters):
    x = random.choice(letters)
    password.append(x)
for i in range(nr_symbols):
    y = random.choice(symbols)
    password.append(y)
for i in range(nr_numbers):
    z = random.choice(numbers)
    password.append(z)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = []
password1 = []
for i in range(nr_letters):
    x = random.choice(letters)
    password1.append(x)
for i in range(nr_symbols):
    y = random.choice(symbols)
    password1.append(y)
for i in range(nr_numbers):
    z = random.choice(numbers)
    password1.append(z)
i = len(password1)
while (i > 0):
    for j in range(len(password1)):
        char = random.choice(password1)
        if (char not in hard_password):
            hard_password.append(char)
            password1.remove(char)
            i -= 1


# Printing of passwords
print("-----Easy Password-----")
for i in password:
    print(i, end='')
print()

print("-----Hard Password-----")
for i in hard_password:
    print(i, end='')
print()
