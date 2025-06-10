from random import choice

from game_data import data
import random
from art import logo
from art import vs

print(logo)

choice_a = random.choice(data)
choice_b = random.choice(data)
score = 0

def for_opt():
    print("Compare A :", choice_a['name'],",",choice_a['description'],",from", choice_a['country'])

def against_opt():
    print("Against B :", choice_b['name'],",",choice_b['description'],",from", choice_b['country'])


def new_choice_a(choice_a, data):
    return random.choice(data)

def new_choice_b(choice_b, data):
    return random.choice(data)

game_continues = True

while game_continues:

    a = choice_a['follower_count']
    b = choice_b['follower_count']

    for_opt()
    print(vs)
    against_opt()

    player = input("Who has more followers? 'A' or 'B':")

    print("\n" * 20)
    print(logo)

    if player == 'a':
        if (a>b) or (a==b):
            score += 1
            print(f"You're right! current score:{score}")
            choice_b =new_choice_b(choice_b,data)
        else:
            print(f"Sorry that's wrong! Final Score:{score}")
            game_continues = False

    elif player == 'b':
        if (b>a) or (a==b):
            score +=1
            print(f"You're right! current score:{score}")
            choice_a = choice_b
            choice_b = new_choice_a(choice_a, data)
        else:
            print(f"Sorry that's wrong! Final Score:{score}")
            game_continues = False






