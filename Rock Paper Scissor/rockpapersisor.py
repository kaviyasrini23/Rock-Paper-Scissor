import random # Importing the random module to allow the computer to make random choices

# Function to determine the winner of the game
def determine_winner(player_choice, computer_choice):
    # If both player and computer choose the same, it's a tie
    if player_choice == computer_choice:
        return "It's a tie!"
    
    # Checking all conditions where the player wins
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    
    # If it's not a tie or player win, then computer wins
    else:
        return "Computer wins!"

# List of possible choices for both player and computer
choices = ['rock', 'paper', 'scissors']

# Infinite loop to keep the game running until the player decides to quit
while True:
    # Asking the player for their choice
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    # If the player types 'quit', the game ends
    if player_choice == 'quit':
        print("Game over!")  # Exiting message
        break  # Breaking the loop to stop the game
    
    # If the player inputs something other than 'rock', 'paper', or 'scissors', it's invalid
    elif player_choice not in choices:
        print("Invalid input! Please choose rock, paper, or scissors.")  # Error message
        continue  # Skipping the rest of the loop and asking for input again

    # The computer randomly chooses between 'rock', 'paper', and 'scissors'
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")  # Displaying the computer's choice

    # Calling the function to determine the winner and printing the result
    result = determine_winner(player_choice, computer_choice)
    print(result)  # Output the result (whether player wins, computer wins, or it's a tie)