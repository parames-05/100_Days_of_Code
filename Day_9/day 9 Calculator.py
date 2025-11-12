logo= '''  

  ________________________________________
 |  _________________________________     |
 | |  Python Calculator v1.0        |  C  |
 | |  >_ Ready to crunch numbers!   |____||
 | |________________________________|____||
 |  ___ ___ ___   ___   ___   ___        |
 | | 7 | 8 | 9 | | + | | ( | | ) |       |
 | |___|___|___| |___| |___| |___|       |
 | | 4 | 5 | 6 | | - | | √ | | ^ |       |
 | |___|___|___| |___| |___| |___|       |
 | | 1 | 2 | 3 | | * | | % | | C |       |
 | |___|___|___| |___| |___| |___|       |
 | | . | 0 | = | | / | | AC| | ⌫ |       |
 | |___|___|___| |___| |___| |___|       |
 |_______________________________________|

'''
print(logo)

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def modulo(n1,n2):
    return n1%n2
def power(n1,n2):
    return n1**n2
def floordiv(n1,n2):
    return n1//n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "%" : modulo,
    "**" : power,
    "//" : floordiv

}

n1= float(input("Enter a number: \n"))
cont= True
while cont:
    n2= float(input("Enter another number: \n"))
    print("Choose an operation to perform + , - , * , / , % , // , **")
    operator= input()
    print(f"{n1} {operator} {n2} = {operation[operator](n1,n2)}")
    ans= operation[operator](n1,n2)
    n1=ans
    aaa=input(f"Enter 'y' to continue with {ans} or enter 'n' to exit the program: \n")
    if aaa == 'n':
        cont = False
        print("Have a nice day")
