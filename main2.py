import random as r
import os
from art import logo

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

blackjack_choice = input('So... do you wanna play some Blackjack?\nEnter "y" if yes, "n" if no...')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
winner = False

copy = []

def blackjack(choice):
    # This is to clear the previous text from the console
    cls()
    print(logo)

    # if choice == 'y':
    #     print(logo)

    # The is going to give the both the user and computer 2 random cards
    user_hand = []
    computer_hand = []
    for i in range(0, 2):
        user_hand.append(r.choice(cards))
        computer_hand.append((r.choice(cards)))

    # These are to record the user and computer's scores
    user_score = 0
    computer_score = 0

    # Below this, I want to enclose the other while loop inside of a while loop that dictates whether the user wants to play again. Possible movement of the cls() function below....

    replay_game = 'y'
    while replay_game == 'y':

        while choice == 'y':
            # Add up scores
            user_score = sum(user_hand)
            computer_score = sum(computer_hand)
            print(f"\t Your cards: {user_hand}, current score: {user_score}")
            print(f"\tComputer's first card: {computer_hand[0]}")

            if (user_score == 21) and (computer_score == 21):
                return "It's a DRAW! 🤯"
            elif (user_score == 21) and (not (computer_score == user_score)):
                return f"Your score is {user_score}! You win! 🤩"
            elif computer_score == 21:
                return 'You lost 😠'

            if user_score > 21:
                if 11 in user_hand:
                    user_hand[user_hand.index(11)] = 1
                    user_score = sum(user_hand)
                    if user_score > 21:
                        return 'You LOST! 😛'
                    elif user_score == 21:
                        return 'You WIN! 🤩'
                    else:
                        print(f"You're ace was swapped, you're safe for now...\nYour score is {user_score}")
                else:
                    return 'You lose!! 😛😛'

            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'y':
                user_hand.append(r.choice(cards))

        # This is testing code to determine why choie == n is causing a hang..
        print(user_score, computer_score)

        # Computer plays now, and keeps drawing cards if score is less than 17
        while computer_score < 17:
            computer_hand.append(r.choice(cards))
            computer_score = sum(computer_hand)
        print(computer_score)

        if computer_score > 21:
            return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nYou win!! 🤩"
        elif user_score < computer_score:
            return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nYou lose. 😛"
        elif user_score > computer_score:
            return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nYou win! 🤩🤩🤩"
        elif computer_score == user_score:
            return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nIt's a DRAW!! 🤯"

        print(computer_score)

        replay_game = input("You want to play some more Blackjack?")

    # while choice == 'y':
    #     # Add up scores
    #     user_score = sum(user_hand)
    #     computer_score = sum(computer_hand)
    #     print(f"\t Your cards: {user_hand}, current score: {user_score}")
    #     print(f"\tComputer's first card: {computer_hand[0]}")
    #
    #     if (user_score == 21) and (computer_score == 21):
    #         return "It's a DRAW! 🤯"
    #     elif (user_score == 21) and (not (computer_score == user_score)):
    #         return f"Your score is {user_score}! You win! 🤩"
    #     elif computer_score == 21:
    #         return 'You lost 😠'
    #
    #     if user_score > 21:
    #         if 11 in user_hand:
    #             user_hand[user_hand.index(11)] = 1
    #             user_score = sum(user_hand)
    #             if user_score > 21:
    #                 return 'You LOST! 😛'
    #             elif user_score == 21:
    #                 return 'You WIN! 🤩'
    #             else:
    #                 print(f"You're ace was swapped, you're safe for now...\nYour score is {user_score}")
    #         else:
    #             return 'You lose!! 😛😛'
    #
    #     choice = input("Type 'y' to get another card, type 'n' to pass: ")
    #     if choice == 'y':
    #         user_hand.append(r.choice(cards))
    #
    # # This is testing code to determine why choie == n is causing a hang..
    # print(user_score, computer_score)
    #
    # # Computer plays now, and keeps drawing cards if score is less than 17
    # while computer_score < 17:
    #     computer_hand.append(r.choice(cards))
    #     computer_score = sum(computer_hand)
    # print(computer_score)
    #
    # if computer_score > 21:
    #     return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nYou win!! 🤩"
    # elif user_score < computer_score :
    #     return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nYou lose. 😛"
    # elif user_score > computer_score:
    #     return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nYou win! 🤩🤩🤩"
    # elif computer_score == user_score:
    #     return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nIt's a DRAW!! 🤯"
    #
    # print(computer_score)
print((blackjack(blackjack_choice)))