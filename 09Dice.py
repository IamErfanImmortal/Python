import random

def roll_dice():
    return random.randint(1, 6)

def check_win(roll1, roll2):
    return roll1 + roll2 == 7

dice_roll1 = roll_dice()
dice_roll2 = roll_dice()

print("First Dice is:",dice_roll1)
print("Second Dice is:",dice_roll2)

if check_win(dice_roll1, dice_roll2):
    print("WIN !!")
else:
    print("Loooser")
