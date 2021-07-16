import random
from os import system
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    """ return a random card from deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# calculate the sum of dealed cards.


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 🙁"
    elif computer_score > 21:
        return "Opponent went over. You win 😎"
    elif user_score > computer_score:
        return "You Win 😁"
    else:
        return "You lose 🙁"


def balckjack():
    print(logo)

    user_card = []
    computer_card = []
    isgameover = False
    # dealing 2 cards to user and computer.
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not isgameover:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"   Your cards: {user_card}, current score: {user_score}")
        print(f"   computer's first cards: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isgameover = True
        else:
            userSholdDeal = input(
                "Type 'y' to get another card,type 'n' to pass: ")
            if userSholdDeal == "y":
                user_card.append(deal_card())
            else:
                isgameover = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"  your final hand: {user_card}  final score: {user_score}")
    print(
        f"  computer's final hand: {computer_card}  final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack? Type 'y' or 'n'") == "y":
    system('clear')
    balckjack()
