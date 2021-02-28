#Coin toss
import random
num = random.randint(0,10)
if num > 5:
    print("Tails")
else:
    print("Heads")

#Russian roulette
names_string = input("Type everybody's names, seperated by comma.\n")
names = names_string.split(",")
    #solution1:
print(random.choice(names))
    #solution2:
num_items = len(names)
random_choice = random.randint(0,num_items-1)
print(names[random_choice])

#
row1 = ["👇","👇","👇"]
row2 = ["👇","👇","👇"]
row3 = ["👇","👇","👇"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("where do you want to hide treasure?\n")

horizontal = int(position[0]) 
vertical = int(position[1]) 

selected_row = map[vertical - 1]
selected_row[horizontal-1] = "X"
#map[vertical - 1][horizontal-1] = "X" alternative

print(f"{row1}\n{row2}\n{row3}\n")

#Rock paper scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
move_list = [rock,paper,scissors]
print("What do you choose? Type 0 for Rock,1 for Paper or 2 For scissors")
move = int(input("Your move:\n"))

if move > 2 or move < 0:
    print("invalid move")
else:
    print(move_list[move])

    player_move = move_list[move]
    ai_move = random.choice(move_list)
    print("ai move:")
    print(ai_move)
    


    if player_move == rock and ai_move == scissors:
        print("you win")
    elif ai_move == rock and player_move == scissors:
        print("You lose")
    elif ai_move > player_move:
        print("You lose")
    elif player_move > ai_move:
        print("You win")
    elif player_move == ai_move:
        print("Tie")
