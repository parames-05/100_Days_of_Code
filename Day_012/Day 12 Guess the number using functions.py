import random
from random import randint

logo = '''
 _______           _______  _______  _______   _________          _______    _                 _______  ______   _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  \__   __/|\     /|(  ____ \  ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/| (    \/| (    \/     ) (   | )   ( || (    \/  |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|
| |      | |   | || (__    | (_____ | (_____      | |   | (___) || (__      |   \ | || |   | || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )     | |   |  ___  ||  __)     | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)
| | \_  )| |   | || (            ) |      ) |     | |   | (   ) || (        | | \   || |   | || |   | || (  \ \ | (      | (\ (   
| (___) || (___) || (____/\/\____) |/\____) |     | |   | )   ( || (____/\  | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__
(_______)(_______)(_______/\_______)\_______)     )_(   |/     \|(_______/  |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/

'''

print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
print("Mode: Easy --- 10 attempts \nMode: Medium --- 7 attempts \nMode: Hard --- 4 attempts")

choice = input("Choose a difficulty: type 'easy' or 'medium' or 'hard'").lower()
num = random.randint(1, 100)

def gamelogic(guess, num):
    if guess == num:
        print("MIND READER MACHINE KILLER!!! YOU WIN!!!")
        return True
    elif guess > num:
        print("Too High!")
    else:
        print("Too Low!")
    return False

def easy(num):
    attempts = 10
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if gamelogic(guess, num):
            break
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    else:
        print(f"You've run out of attempts. The number was {num}.")

def medium(num):
    attempts = 7
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if gamelogic(guess, num):
            break
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    else:
        print(f"You've run out of attempts. The number was {num}.")

def hard(num):
    attempts = 4
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if gamelogic(guess, num):
            break
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    else:
        print(f"You've run out of attempts. The number was {num}.")

if choice == "easy":
    easy(num)
elif choice == "medium":
    medium(num)
elif choice == "hard":
    hard(num)
else:
    print("Invalid difficulty selected!")

