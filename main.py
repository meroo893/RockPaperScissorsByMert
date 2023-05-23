import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

followup = True
while followup:
    player_move = input("Choose [r]ock, [p]aper, [s]cissors>>  ")
    while player_move.lower() != "r" and player_move.lower() != "p" and player_move.lower() != "s" and \
            player_move.lower() != "rock" and player_move.lower() != "paper" and player_move.lower() != "scissors":
        print("Invalid input!")
        player_move = input("Choose [r]ock, [p]aper, [s]cissors >>  ")

    if player_move.lower() == "r" or player_move.lower() == "rock":
        player_move = rock
    elif player_move == "p" or player_move.lower() == "paper":
        player_move = paper
    else:
        player_move = scissors

    random_num = random.randint(1, 3)
    comp_move = ""
    if random_num == 1:
        comp_move = rock
    elif random_num == 2:
        comp_move = paper
    else:
        comp_move = scissors

    print(f"I choose {comp_move.title()}")
    print(f"You chose {player_move.title()}")

    if (player_move == rock and comp_move == scissors) or (player_move == paper and comp_move == rock) \
            or (player_move == scissors and comp_move == paper):
        print("You win!")
    elif (player_move == rock and comp_move == rock) or (player_move == paper and comp_move == paper) \
            or (player_move == scissors and comp_move == scissors):
        print("It's a draw!")
    else:
        print("You lose!")
    flwp = input("Do you want to play again: [y]es or [n]o >> ")
    if flwp.lower() == "y" or flwp.lower() == "yes":
        followup = True
    elif flwp.lower() == "n" or flwp.lower() == "no":
        followup = False
        print("Thank you for the game!")
    else:
        print("Invalid input!")
        flwp = input("Do you want to play again: [y]es or [n]o >> ")