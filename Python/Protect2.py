#This is a mini version of the game "liar's dice", from the movie Pirates of the Carribean: Dead Man's Chest
#The goal of the game is to guess how many of a certain dice are at the table. Davy will give a bluff or real answer, and the player must determine if he's lying by looking at their own dice.
#The player is guessing if the number of the dice is higher, lower, or equal to what davy says.
#Rules on the game can be found at https://www.youtube.com/watch?v=fAbnMuiR734&t=64s

import random
import time
from collections import Counter

#Rolls two sets of 5 dice, one for the player and one for Davy Jones.
number_dice = 5
player_dice_value = [random.randint(1, 6) for _ in range(number_dice)]
davy_jones_value = [random.randint(1, 6) for _ in range(number_dice)]

#Tells the player what dice they rolled
print("Rolling your dice...")
time.sleep(1)
print("You have rolled...")
for dice in player_dice_value:
    print(dice)

#Counts how many of a certain value that Davy Jones has rolled. Most common count stores how many of a dice are rolled. Most common number stores the actual value, 1-6, of the dice.
davy_dice_counts = Counter(davy_jones_value)
most_common_count = davy_dice_counts.most_common(1)[0][1]
most_common_numbers = [num for num, count in davy_dice_counts.items() if count == most_common_count]

#Handles exceptions if there is most than 1 most common dice value. Selects just a random dice value from the most common.
if len(most_common_numbers) > 1:
    most_common_numbers = random.choice(most_common_numbers)
else:
    most_common_numbers = most_common_numbers[0]

#This counts what the most common dice is at the table, the one that Davy will tell the player, and keeps track of how many are actually at the table.
#Let's game find out if he's lying.
total_most_common_number = most_common_count
for dice in player_dice_value:
    if dice == most_common_numbers:
        total_most_common_number += 1

#This adds a random value to the most common count. This is where the challenge of the game is created, as Davy will randomly add a certain amount of dice to his guess.
davy_jones_says = most_common_count / 2
if davy_jones_says % 2 != 0:
    davy_jones_says += 1
davy_jones_bluff = davy_jones_says + random.randint(1, 3)


#Asking the player to guess
print(f"Davy Jones claims there are at least {int(davy_jones_bluff)} {most_common_numbers}'s at the table. Is he lying? Y/N")
answer = input(str())

#Ensures a proper answer was given before continuing
answer = answer.lower()
while True:
    if answer == "y":
        break
    elif answer == "n":
        break
    else:
        print("Please only enter Y or N")

#Determines if you've won the game.
if davy_jones_bluff < total_most_common_number or davy_jones_bluff == total_most_common_number and answer == "n":
    print("Correct, he was telling the truth. You've beat the devil, congratulations!")
elif davy_jones_bluff < total_most_common_number or davy_jones_bluff == total_most_common_number and answer == "y":
    print("Incorrect, he was telling the truth, he's won your soul...")
elif davy_jones_bluff > total_most_common_number and answer == "y":
    print("Correct, you've caught his lie! You've beat the devil, congratulations!")
else:
    print("Incorrect, you fell for his lie, he's won your soul...")
    
time.sleep(5)