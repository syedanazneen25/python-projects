import random
from hangman_logo import logo
from hangman_logo import stages
from hangman_word import word_list

print(logo)
print("Welcome to the hangman game!!!")
lives = 6



display = []
chosen_word = random.choice(word_list)
for letter in chosen_word:
    display.append("_")
#print(chosen_word)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    if guess not in chosen_word:
        print(f"{guess} is not in the word.")
        lives-=1
        if lives == 0:
            end_of_game = True
            print("You're out of lives...")
            print(f"The word is {chosen_word}.")
            print("You lose!")
    print(f"{' '.join(display)}")
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You win.")
    