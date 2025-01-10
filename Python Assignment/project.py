# Rock Paper Scissors Game

import random # random model is used to choose random option

options = ("rock", "paper", "scissors") # Using tuples because we are not going to change the options 
playing = True # variable to control loop

while playing:
    player = None # variable name player to store the player choice
    computer = random.choice(options) # computer will pick random choice from the option
    playing = True  # Ensure the game continues unless explicitly ended

     # Loop to ensure the player enters a valid choice
    while player not in options: 
        player = input("Enter your choice (rock, paper, scissors): ")
        if player not in options:
            print("Please enter a valid option: rock, paper or scissors. ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

  # Determine the result of the game based on the rules
    if player == computer:
        print("It's a tie!!")
    elif player == "rock" and computer == "scissors":
        print("You Win !!")
    elif player == "paper" and computer == "rock":
        print("You Win!!")
    elif player == "scissors" and computer == "paper":
        print("You Win!!")
    else:
        print("You Lose!!")

 # Asing user to continue gamer or not
    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again == "y": # if yes, break and restart game
            break
        elif play_again == "n":
            play_again = False # if no end program
            break
        else:  # ensure correct option is entered
            print("Please enter 'y' for continue playing and 'n' for end game.")

print("Thanks for playing!!")


