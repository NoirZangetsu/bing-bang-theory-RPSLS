import random
import emoji

print("Let's play rock-paper-scissors-lizard-Spock!")

options = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
symbols = {'rock': emoji.emojize('\U0001F5FB'),
           'paper': emoji.emojize('\U0001F4C4'),
           'scissors': emoji.emojize('\U00002702'),
           'lizard': emoji.emojize('\U0001F98E'),
           'Spock': emoji.emojize('\U0001F596')}

rules = {'rock': ['scissors', 'lizard'],
         'paper': ['rock', 'Spock'],
         'scissors': ['paper', 'lizard'],
         'lizard': ['paper', 'Spock'],
         'Spock': ['rock', 'scissors']}

while True:
    player_choice = input("Enter your choice (rock/paper/scissors/lizard/Spock): ")
    if player_choice not in options:
        print("Invalid input. Please try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose {symbols[computer_choice]}.")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif computer_choice in rules[player_choice]:
        print(f"{symbols[player_choice]} beats {symbols[computer_choice]}. You win!")
    else:
        print(f"{symbols[computer_choice]} beats {symbols[player_choice]}. Computer wins!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again != 'y':
        break

print("Thanks for playing!")
