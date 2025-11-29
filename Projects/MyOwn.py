from MyOwn1 import*

while True:
  Chosen_Player = input("choose your player [archer] OR [knight]:")

  if Chosen_Player == Player_one.lower():
    print("You are an Archer")
    break

  elif Chosen_Player == Player_two.lower():
    print("You are a Knight")
    break

  else:
    print("Please enter valid player")
    
while True:
  Character_Name = input("Enter the name of your character: ")

  if Character_Name.isalpha():
    print(f"Your name is {Character_Name}")
    break
      
  else:
    print("The name must contain only Alphabets")
  

while True:
 items = (input("menu1 for archer and menu2 for knight to open Inventory: "))

 if Chosen_Player == "archer":
  if items == Inventory1:
    print(menu1)
    break
  else:
     print("Please enter the correct menu")
    
 elif Chosen_Player == "knight":
    if items == "menu2":
     print(menu2)
    break
    
 else:
    print("Please enter the correct menu")
    
 
while True:
    Mission = input(f"DESTROY ALL ZOMBIES {Character_Name}: ").lower()

    if Mission == Forward:
        print("You moved forward")

    elif Mission == Backward:
        print("You moved backward")

    elif Mission == Left:
        print("You moved towards left")

    elif Mission == Right:
        print("You moved towards right")

    elif Mission == Attack:
        zombies -= 1
        Kills = "Danger Ahead" if zombies >= 10 else "Nice Job!"
        print("You killed a zombie!")
        print(Kills)

        if zombies == 0:
            print("All zombies defeated!")
            print("MISSION SUCCESSFULL!!")
            break

    else:
        print("Invalid move! Try again.")










    
















