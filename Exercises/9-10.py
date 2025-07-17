import random

class Die:
    def __init__(self, sides = 10):
        self.sides = sides

    def roll_dice(self):
        print(f"Welcome To the {self.sides} Dice game!")
        tries = 0
        while tries <=9:
            user_answer = input("Do you wish to roll the dice 😊 (yes/no): ")
            if user_answer == "yes":
                roll = random.randint(1,self.sides)
                tries += 1
                print(f"{roll}")
            elif user_answer == "no":
                print("Exciting the Game!\n")
                break
            else:
                print("Invalid Input! Try Again.")

