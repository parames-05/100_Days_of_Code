import random as rrr
from random import randrange

logo= '''
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
print("\n Welcome to the number guessing game \n I am thinking of a number between 1 and 100")
print("Mode: Easy --- 10 attempts \n Mode : Medium --- 7 attempts \n Mode : Hard --- 4 attempts")
choice = input("Choose a difficulty type 'easy' or 'medium' or 'hard' \n").lower()
if choice == "easy":
    num = randrange(1,101)
    i=10
    while i != 0:
        guess = int(input("\nGuess a number: "))
        if guess == num:
            print("You are a mindreader, machine killer!!! YOU WINNNN!!!")
            break
        elif guess > num:
            print("Too high")
            i -= 1
            print(f"You have {i} attempts left")
        else:
            print("Too Low")
            i -= 1
            print(f"You have {i} attempts left")
        if i == 0:
            print(f"You have exhausted all your attempts, the number was {num}")
elif choice == "medium":
    num = randrange(1, 101)
    i = 7
    while i != 0:
        guess = int(input("\nGuess a number: "))
        if guess == num:
            print("You are a mindreader, machine killer!!! YOU WINNNN!!!")
            break
        elif guess > num:
            print("Too high")
            i -= 1
            print(f"You have {i} attempts left")
        else:
            print("Too Low")
            i -= 1
            print(f"You have {i} attempts left")
        if i == 0:
            print(f"You have exhausted all your attempts, the number was {num}")
else:

    num = randrange(1, 101)
    i = 4
    while i != 0:
        guess = int(input("\nGuess a number: "))
        if guess == num:
            print("You are a mindreader, machine killer!!! YOU WINNNN!!!")
            break
        elif guess > num:
            print("Too high")
            i -= 1
            print(f"You have {i} attempts left")
        else:
            print("Too Low")
            i -= 1
            print(f"You have {i} attempts left")
        if i == 0:
            print(f"You have exhausted all your attempts, the number was {num}")