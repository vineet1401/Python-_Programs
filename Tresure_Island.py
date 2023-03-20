print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
loop = True
while (loop):
    direction = input(
        "You\'re at the crossroad. Choose where  you want to go? type Left or Right : ")

    if (direction.lower() == "left"):
        print("You\'ve come to a lake. There is an island in the middle of the lake. Type \'wait\' to wait for a boat.   Type \'swim\' to swim across.")

        choice = input("Your choice : ")

        if (choice.lower() == "swim"):
            print("You arrive at the island unharmed. There is a  house with 3 doors. One red, one yellow and one blue.      Which colour do you choose?")

            colour = input("Choose Colour : ")

            if (colour.lower() == "red"):
                print("You found the treasure! You Win!")
                loop = False
            elif (colour.lower() == "yellow"):
                print("You enter a room of beasts. Game Over.")
                loop = False
            elif (colour.lower() == "blue"):
                print("It's a room full of fire. Game Over.")
                loop = False
            else:
                print("You chose a door that doesn't exist. Game  Over.")
                loop = False

        else:
            print("You fell into a hole. Game Over.")
            loop = False

    else:
        print("You get attacked by an angry trout. Game Over.")
        loop = False
