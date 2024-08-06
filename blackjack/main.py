import random


logo = r'''
.------.              _     _            _    _            _    
|A_  _ |             | |   | |          | |  (_)          | |   
|( \/ ).-----.       | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |       | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |       | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |       |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                              _/ |                
      `------'                             |__/          
      '''
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "You win with a blackjack"
    elif computer_score == 0:
        return "You lose computer has blackjack"
    elif user_score > 21:
        return "You went over 21, you lose"
    elif computer_score > 21:
        return "You win! computer went over"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():

    game_over = False
    computer_score = -1
    user_score = -1
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())



    while not game_over:
        print(logo)
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)
        print(f"Your cards are {user_cards} and your total is: {user_score}.")
        print(f"Computer's first card is: {computer_cards[0]}.")

        if user_score == 21 or computer_score == 0 or user_score > 21:
            game_over = True
        else: 
            add_card = input("Type 'y' to get another card or type 'n' to pass:" )
            if add_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = sum(computer_cards)

    print(f"Your final deck is {user_cards} and final score is {user_score}")
    print(f"Computer final deck is {computer_cards} and final score is {computer_score}")

    print(compare(user_score, computer_score))


while input("Do you want to play game:'y' or 'n': \n") == "y":
    print("\n" * 20)
    play_game()