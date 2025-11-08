import random as rrr

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?\n"))
sym = int(input("How many symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))

# Get random choices
ch1 = rrr.choices(letters, k=let)
ch2 = rrr.choices(numbers, k=num)
ch3 = rrr.choices(symbols, k=sym)

# Combine all into one flat list
aaa = ch1 + ch2 + ch3

# Shuffle in-place
rrr.shuffle(aaa)

# Build final password string
ccc = ""
for item in aaa:
    ccc += item

print(f"Your password is: {ccc}")