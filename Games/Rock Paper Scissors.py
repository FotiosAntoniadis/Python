import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("Rock, Paper or Scissors? ").lower()

    if player == computer:
        print("Computer: " + computer)
        print("Player: " + player)
        print("It's a Tie!")
    # My way:
    # elif player == "scissors" and computer == "paper":
    #     print("haha")
    # Bro Code's way:
    elif player == "scissors":
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You win")
        if computer == "rock":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You lose")

    elif player == "rock":
        if computer == "scissors":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You win")
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You lose")

    elif player == "paper":
        if computer == "rock":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You win")
        if computer == "scissors":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You lose")

    play_again = input("Do you want to play again? (Yes/No) : ").lower()

    if play_again != "yes":
        break
print("Bye!")

# 03/07/23