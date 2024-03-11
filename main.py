import random 
import os
from time import sleep

print(len("Welcome To My Dice Roll Game :)")*"x",'\n'"Welcome To My Dice Roll Game :)"'\n',"x"*len("Welcome To My Dice Roll Game :)"))

name = input("please enter your name: ")
print(f"Hello {name} I wish you success :)")

sleep(5)

def Num_Die():
    while True:
        try:
            answer = input("do you want to play with (1 die or 2 dice): ").lower()
            valid_ans = ['1','2','one','two']
            if answer not in valid_ans:
                raise ValueError("only 1 or 2")
            else:
                return answer
        except ValueError as error:
            print(error)


def Roll_Dice():
    min_val = 1
    max_val = 6 
    answer = 'yes'

    while answer == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = Num_Die()

        if amount == "1" or amount == 'one':
            print("Rolling the die... ")
            sleep(2)
            dice_1 = random.randint(min_val,max_val)
            print(f'the value is: {dice_1}')

            answer = input("Do You Want To Roll Again (yes,no): ").lower()
        else:
            print("Rolling the dice... ")
            sleep(4)
            dice_1 = random.randint(min_val,max_val)
            dice_2 = random.randint(min_val,max_val)

            print(f"The first value is {dice_1}")
            print(f"The second value is {dice_2}")
            print(f"The total is {dice_1 + dice_2}")

            answer = input("Do You Want To Roll Again (yes,no): ").lower() 

if __name__ == '__main__':
    Roll_Dice()
# This Is My Dice_Roll_Generator_Project
