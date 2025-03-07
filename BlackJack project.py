from traceback import print_exc
from art import logo
import random

def deal_card():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card

def calculate_score(deck):
    """Takes a list of cards and returns the score calculated from cards"""
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if sum(deck) >21 and 11 in deck :
        deck.remove(11)
        deck.append(1)
    return sum(deck)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw."
    elif c_score == 0:
        return "You Lose! The opponent has a Blackjack"
    elif u_score == 0:
        return " You win with a Blackjack!"
    elif u_score > 21:
        return "You went over You Lose!"
    elif c_score > 21:
        return "The opponent over You Win!"
    elif u_score == 21:
        return "You Win"
    elif c_score == 21:
        return "You Lose"
    elif u_score > c_score:
        return "YOu Win!"
    else:
        return "You lose!"

def play_game():

    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Your score: {user_score} ")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            ask_user = input("Type 'y' to get another card or 'n' to Pass:")
            if ask_user == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, Your Score:{user_score}")
    print(f"Computer's final hand:{computer_cards}, computer's score:{computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack Type 'y' or 'n':") == 'y':
    print(logo)
    print("\n"*30)
    play_game()