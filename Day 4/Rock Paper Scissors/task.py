import random

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
#my code
Choice1 = [rock,paper,scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper,and 2 "
          "for Scissors\n"))
Computer_choice = random.randint(0,2)
if choice==0:
    print("You Choose:")
    print(rock)
    print("computer choose:")
    print(Choice1[Computer_choice])
    if Computer_choice== 0:
        print("Its a draw")
    elif Computer_choice== 2:
        print("You win!")
    elif Computer_choice==1:
        print("You loose!")
elif choice==1:
    print("You Choose:")
    print(paper)
    print("computer choose:")
    print(Choice1[Computer_choice])
    if Computer_choice== 1:
        print("Its a draw")
    elif Computer_choice== 2:
        print("You loose!")
    elif Computer_choice==0:
        print("You Win!")
elif choice==2:
    print("You Choose:")
    print(scissors)
    print("computer choose:")
    print(Choice1[Computer_choice])
    if Computer_choice== 2:
        print("Its a draw")
    elif Computer_choice== 1:
        print("You win!")
    elif Computer_choice==0:
        print("You loose!")

#option of angela
rps = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for rock,1 for paper and 2 for scissors\n"))
if user_choice>=0 and user_choice<=2:
    print(rps[user_choice])
computer_choice = random.randint(0,2)
print("computer choose:")
print(rps[computer_choice])
if user_choice>=3 or user_choice<0:
    print("Invalid number!")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif computer_choice==0 and user_choice==2:
    print("You lose!")
elif computer_choice> user_choice:
    print("You lose!")
elif user_choice> computer_choice:
    print("You win!")
elif computer_choice==user_choice:
    print("its a draw!")
