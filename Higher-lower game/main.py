from art import logo, vs
from data import data
import random
print(logo)
choice_a = random.choice(data)
choice_b = random.choice(data)
choice_a_follower = choice_a['follower_count']
choice_b_follower = choice_b['follower_count']
current_score = 0

game_end = False
while not game_end:
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
    print(vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice_a_follower > choice_b_follower and user_guess == "a":
        current_score += 1
        print(f"You are right. Current score: {current_score}")
        choice_a = choice_b
        if choice_b == choice_a:
            choice_b = random.choice(data)


    elif choice_a_follower < choice_b_follower and user_guess == "b":
        current_score += 1
        print(f"You are right. Current score: {current_score}")
        choice_a = choice_b
        choice_b = random.choice(data)
        if choice_b == choice_a:
            choice_b = random.choice(data)

    else:
        game_end = True
        print(f"Wrong answer. Final score: {current_score}")
