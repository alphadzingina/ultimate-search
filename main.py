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

print("Welcome to Ultimate Search!")
print("You're on the island of Dzadzakun. Your mission is to find Alpha's lost treasure.")
print("Goodluck")
choice1 = input("You\'re at a crossroad. Where do you want to go? Type 'left' or 'right':\n")
if choice1 == "right":
    print("You fell into a hole. Game Over")
else:
    choice2 = input("You\'ve come to a lake.\nThere is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across:\n")
    if choice2 == "swim":
        print("You got attacked by trouts. Game Over")
    else:
        choice3 = input("You arrive at the island unharmed.\nThere is a house with 3 doors. One red, one yellow and one blue.\nWhich colour do you choose?:\n")
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! Congratulations! You're the ultimate man!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

print("The Game has ended")

