# import th erandom package so that we can generate random numbers
from random import randint

# choices is as array => a container that can hold multiple items
# arrays are 0-based => the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer choose a weapon from the coices array at random
computer_choice = choices[randint(0, 2)]

# print the choice to the terminal window
print("Computer chooses: ", computer_choice)

# set up a loop
while player is False:
    # set player to true by making a selecion
    print("Choose your weapon!")
    player = input("Rock, Paper or Scissors?\n")

    print(player, "\n")

    # check fro a tie = coices are the same
    if computer_choice == player:
        print("Tie! You live to shoot another day")
    # check to see if computer hoise beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            print("You lose! Paper covers Rock")
        else:
            print("You win! Rock crushes Scissors")

    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You lose! Rock crushes Scissors")
        else:
            print("You win! Scissors cuts Paper")

    elif player == "Paper":
        if computer_choice == "Scisors":
            print("You lose! Scissors cut Paper")
        else:
            print("You win! Paper covers Rock")
    elif player == "quit":
        exit()
    else:
        print("Check your spelling... that's not avalid choice\n")

    # reset the game loop and start over again
    player = False
    computer_choice = choices[randint(0, 2)]
