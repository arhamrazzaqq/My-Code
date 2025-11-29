menu = {"burger": 5.00,
        "fries": 2.50,
        "soda": 1.75}
cart = []
total = 0
print("Welcome to the Concession Stand!")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("----------------------------")

while True:
    food = input("Enter the food item you want to order (or 'q' to finish): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
     cart.append(food)
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is: ${total:.2f}")



       
