import random as rrr
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice=int(input("Enter a number \n 0 for rock \n 1 for paper \n 2 for scissors\n"))
if choice==0:
    print("User chooses:",rock)
elif choice==1:
    print("User chooses:", paper)
elif choice == 2:
    print("User chooses:",scissors)
else:
    print("Out of index number enter between 0 to 2")

com=rrr.randint(0,2)
if com == 0:
    print("Computer chooses:",rock)
elif com == 1:
    print("Computer chooses:", paper)
else:
    print("Computer chooses:", scissors)

if choice==0 and com == 0:
    print("Tie, try again")
elif choice ==1 and com == 1:
    print("Tie, try again")
elif choice == 2 and com == 2:
    print("Tie, try again")
else:
    if choice ==0 and com ==1:
        print("computer wins :(")
    if choice==0 and com ==2:
        print("User wins :)")
    if choice == 1 and com ==0:
        print("User wins :)")
    if choice == 1 and com ==2:
        print("Computer wins :(")
    if choice == 2 and com == 0:
        print("Computer wins :(")
    if choice == 2 and com == 1:
        print("User wins :)")
        #0= rock   1 = paper 2 = scissors
print("Have a nice dayyyyyyy")