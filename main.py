# It's a program about rock paper scissors game.
# Algorithm:
# 1. Find players
# 2. Explain rules
# 3. Start the game
# 4. Get player's choice
# 5. Get computer's choice
# 6. Compare and find out who is the winner
# 7. Ask player if they want to play again


import random
# 1. Find players
player_name = input("Enter your name: ")
print(f"Hello, {player_name}! Let's play rock-paper-scissors!")

# 2. Explain rules
print("\nHere are the rules:")
print("1. Rock beats scissors")
print("2. Scissors beats paper")
print("3. Paper beats rock")

# 3. Start the game
while True:
    print("Rock, paper, scissors, shoot!")
    # 4. Get player's choice'
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Your choice (rock, paper, scissors): ").lower()
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
   # 5. Get computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")
   # 6. Compare and find out who is the winner
    if player_choice == computer_choice:
      print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "scissors" and computer_choice == "paper") or \
        (player_choice == "paper" and computer_choice == "rock"):
            print("You win!")
    else:
            print("You lose!")
    # 7. Ask player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again!= "yes":
        break


