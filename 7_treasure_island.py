print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("\tWelcome to tresure island!\n\tYour mission is to find the tresure.\n")
a = input("You're at a cross road. Where do you want to go?\n\t Type \"left\" or \"right\"\n")
a = a.lower()
if a == "left":
    b = input("You're come to a lake. There is an island in the middle of lake. \n\tType 'wait' to wait for a boat. Type 'swim' to swim across.\n")

    if b == "wait":
        door = input("There are three doors. Choose one \n\t'red'    'yellow'    'blue'\n")
        door = door.lower()

        if door == "blue":
            print("Hurrey!! You got treasure and won the game.")
        elif door == "red":
            print("You fell into lawa and lost \nGame over :(") 
        else: print("This is not your day. Now you are into dragons house :(")      
    else:print("Game over you got killed by a tsunami. \nGame over. :(")     

else: 
    print("You fell into a hole. Game over. :( ")






