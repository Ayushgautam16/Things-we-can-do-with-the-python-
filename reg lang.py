import random
def get_player_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")\
            