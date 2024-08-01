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

print("Welcome to Rock-Paper-Scissor Game..")

user_choice = int(input("Choose 0 for Rock, 1 for Paper, or 2 for Scissor:\n"))
computer_choice = random.choice(range(0,3))
print(f"Your choice is {user_choice}.")
print(f"Computer's choice is {computer_choice}.")

if user_choice == 0 and computer_choice == 1:
    print("Your choice is Rock.")
    print(rock)
    print("Computer's choice is Paper.")
    print(paper)
    print("You lose.")
elif user_choice == 1 and computer_choice == 2:
    print("Your choice is Paper.")
    print(paper)
    print("Computer's choice is Scissor.")
    print(scissors)
    print("You lose.")
elif user_choice == 2 and computer_choice == 0:
    print("Your choice is Scissor.")
    print(scissors)
    print("Computer's choice is Rock.")
    print(rock)
    print("You lose.")
elif user_choice == 0 and computer_choice == 2:
    print("Your choice is Rock.")
    print(rock)
    print("Computer's choice is Scissor.")
    print(scissors)
    print("You won.")
elif user_choice == 1 and computer_choice == 0:
    print("Your choice is Paper.")
    print(paper)
    print("Computer's choice is Rock.")
    print(rock)
    print("You won.")
elif user_choice == 2 and computer_choice == 1:
    print("Your choice is Scissor.")
    print(scissors)
    print("Computer's choice is Paper.")
    print(paper)
    print("You won.")
elif user_choice == computer_choice:
    print("Its a draw.")