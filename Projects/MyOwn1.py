import MyOwn
#MENU
print("*******************************")
print(" ")
print("WELCOME TO MY GAME!")
print("YOU ARE PLAYING ZOMBIE KILLER!")
print("*******************************")
print("Press W to move forward and S to move backwards")
print("A or D to move left and right")
print("*******************************")

zombies = 10
Character_Name = []
Player_one = ("archer")
Player_two = ("knight")
Health = 100
Attack = "e"
damage = 10
Forward = "w"
Backward = "s"
Left = "a"
Right = "d"
Inventory1 = ("menu1")
Inventory2 = ("menu2")
menu1 = ("[Arrows: 25]"
        "[Potion of Healing: 3]")
menu2 =  ("[knifes: 25]"
          "[Potion of Healing: 3]")
archer = (f"{Player_one} {menu1}")
knight = (f"{Player_two} {menu2}")