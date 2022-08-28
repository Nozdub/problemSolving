# --------------------------------------------- Rock, paper scissors --------------------------------------------------#
import random


# Making main play function with if statements regarding game outcome:
def play():
    user = input("What's your choice (rock, paper, scissors): ")
    computer = random.choice(["rock", "paper", "scissors"])

    if user == computer:
        return f"You both selected {user}, so it's a tie"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You won!"

    return "You lost"


# Defining what a win is:
def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == "rock" and opponent == "scissors") or (player == "paper" and opponent == "rock") \
            or (player == "scissors" and opponent == "paper"):
        return True

# Created a loop for the game that plays as long as the answer to continue is something else than no.
start = input("Do you want to play a game of rock, paper, scissors? (yes/no): ")
if start == "yes":
    while start:
        print(play())
        cont = input("Play another round? (yes/no): ")
        if cont == "no":
            break


