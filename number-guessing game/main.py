import random
EASY_TURNS = 10
DIFFICULT_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    elif user_guess == actual_answer:
        print(f"{actual_answer}. Correct Answer!! ")

def difficulty_level():
    level = input("Choose a difficulty level. Easy or Hard ?\n").lower()
    if level == "easy":
        global turns
        return EASY_TURNS
    elif level == "hard":
        return DIFFICULT_TURNS

def game():

    print("Welcome to the number guessing game!!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    turns = difficulty_level()
    guess = 0 
    while guess != number:
        print(f"You have {turns} guesses to guess the number.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You ran out of guesses. You lose!!")
            return
        elif guess != number:
            print("Guess again.")


game()