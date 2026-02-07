import random

win_number = [7, 11]
craps_number = [2, 3, 12]
goal_number = [4, 5, 6, 8, 9, 10]

def random_numbers():
    first_num = random.randint(1, 6)
    second_num = random.randint(1, 6)
    return first_num, second_num

dice = random_numbers()
print(f"The sum of dice is {dice[0]} + {dice[1]} = {dice[0] + dice[1]}")
if dice[0] + dice[1] in win_number:
    print("You won")
elif dice[0] + dice[1] in craps_number:
    print("You lose")
elif dice[0] + dice[1] in goal_number:
    goal = dice[0] + dice[1]
    print(f"Now your goal number is  {goal}")
    dice = random_numbers()
    while dice[0] + dice[1] != goal:
        dice = random_numbers()
        print(f"The sum of dice is {dice[0]} + {dice[1]} = {dice[0] + dice[1]}")
        if dice[0] + dice[1] == goal:
            print("You won")
            break
        elif dice[0] + dice[1] == 7:
            print("You lose")
            break