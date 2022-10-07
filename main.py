############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
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
    # while replay_game == 'y':
    #
    #     replay_game = input('Hey 👀, you wanna play Blackjack aga in?\n\tType "y" to continue')

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

    # Computer plays now, and keeps drawing cards if score is less than 17
    while computer_score < 17:
        computer_hand.append(r.choice(cards))
        computer_score = sum(computer_hand)

    if computer_score > 21:
        return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nYou win!! 🤩"
    elif user_score < computer_score :
        return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nYou lose. 😛"
    elif user_score > computer_score:
        return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nYou win! 🤩🤩🤩"
    elif computer_score == user_score:
        return f"\tYour final hand: {user_hand}, final score {user_score}\n\tComputer's final hand: {computer_hand}, final score {computer_score}\nIt's a DRAW!! 🤯"

    print(computer_score)

if blackjack_choice == 'y':
    print((blackjack(blackjack_choice)))
else:
    print('Maybe some other time...')

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
