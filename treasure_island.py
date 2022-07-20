
'''                                                                      
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88                                                                             
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
'''

print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")
choice1 = input("You are at a cross road. Where do you want to go? Enter Left or Right: ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an Island in the middle of the lake. Enter Swim or Wait to cross over to the other side:").lower()
    if choice2 == "wait":
        choice3 = input('You\'re at the Island now and there are 3 doors. Which door would you want to open? Enter "Red", "Yellow" or "Blue": ').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game over!")
        elif choice3 == "yellow":
            print("You've found the treasure. You won!")
        elif choice3 == "blue":
            print("You've entered a room full of beasts. Game over!")
        else:
            print("You chose a door that doesn't exist. Game over!")
    else:
        print("You got attacked by an angry Crocodile. Game over!")
else:
    print("You fell into a hole. Game over!")