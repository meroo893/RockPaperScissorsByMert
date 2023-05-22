import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper, [s]cissors>>  ")
while player_move.lower() != "r" and player_move.lower() != "p" and player_move.lower() != "s":
    print("Invalid input!")
    player_move = input("Choose [r]ock, [p]aper, [s]cissors>>  ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
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
