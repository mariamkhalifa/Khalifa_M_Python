# import the random package so that we can generate random numbers
from random import randint

# choices is as array => a container that can hold multiple items
# arrays are 0-based => the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False
computer_lives = 3
player_lives = 3
winner = "none"
new_computer_lives = 3
new_player_lives = 3

# print title
print("\nRock Paper Scissors Game")
print("************************")
# make the computer choose a weapon from the coices array at random
computer_choice = choices[randint(0, 2)]

# set up a loop
while player is False:
    # set player to true by making a selecion
    print("\nChoose your weapon!")
    player = input("Rock, Paper or Scissors?\n")

    # check fro a tie = coices are the same
    if computer_choice == player:
        print("\n**Tie! You live to shoot another day")
        winner = "none"

    # check to see if computer choise beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            print("\n**You Lose! Paper covers Rock")
            winner = "computer"

        else:
            print("\n**You win! Rock crushes Scissors")
            winner = "user"

    elif player == "Scissors":
        if computer_choice == "Rock":
            print("\n**you lose! Rock crushes Scissors")
            winner = "computer"

        else:
            print("\n**You win! Scissors cuts Paper")
            winner = "user"

    elif player == "Paper":
        if computer_choice == "Scisors":
            print("\n**You lose Scissors cut Paper")
            winner = "computer"

        else:
            print("\n**You win! Paper covers Rock")
            winner = "user"

    elif player == "quit":
        exit()

    else:
        print("\nCheck your spelling... that's not a valid choice\n")

    if winner == "user":
        new_player_lives = player_lives
        new_computer_lives = computer_lives - 1

    elif winner == "computer":
        new_player_lives = player_lives - 1
        new_computer_lives = computer_lives

    elif winner == "none":
        new_player_lives = player_lives
        new_computer_lives = computer_lives

    print("\nPlayer Lives Remaining: ", new_player_lives)
    print("Computer Lives Remaining: ", new_computer_lives)

    player_lives = new_player_lives
    computer_lives = new_computer_lives

    if new_player_lives == 0:
        print("\n**Game Over**! \nYou Lose!")
        print("Would you like to play again?")
        player = input("yes, quit\n")
        if player == "yes":
            player = False
            computer_choice = choices[randint(0, 2)]
            player_lives = 3
            computer_lives = 3
        elif player == "quit":
            exit()

    if new_computer_lives == 0:
        print("\n**Game Over**! \nYou Win!")
        print("Would you like to play again?")
        player = input("yes, quit\n")
        if player == "yes":
            player = False
            computer_choice = choices[randint(0, 2)]
            player_lives = 3
            computer_lives = 3
        elif player == "quit":
            exit()

    # reset the game loop and start over again
    player = False
    computer_choice = choices[randint(0, 2)]
