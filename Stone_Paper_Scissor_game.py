import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

user = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
comp = random.randint(0, 2)

if (user == 0):
    userin = rock
elif (user == 1):
    userin = paper
else:
    userin = scissors

if (comp == 0):
    compin = rock
elif (comp == 1):
    compin = paper
else:
    compin = scissors

print(f"You Choose : {userin}")
print(f"Computer Choose : {compin}")
print("----------Score----------")

if ((userin == rock) and (compin == rock)):
    print("Tie")
elif ((userin == rock) and (compin == paper)):
    print("You lose")
elif ((userin == rock) and (compin == scissors)):
    print("You Won")
elif ((userin == scissors) and (compin == rock)):
    print("You lose")
elif ((userin == scissors) and (compin == paper)):
    print("You Won")
elif ((userin == scissors) and (compin == scissors)):
    print("Tie")
elif ((userin == paper) and (compin == rock)):
    print("You Won")
elif ((userin == paper) and (compin == paper)):
    print("Tie")
else:
    print("You lose")
