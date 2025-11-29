foods = []
prices = []
total = 0

while True:
    food = input("Enter the food to perchase (q to quit):")
    if food.lower() == "q":
        break
    else:
        foods.append (food)
        price = float(input(f"Enter the price of {food}: $"))
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(food)
for pice in prices:
    total += price

print(f"Total: ${total:.2f}")

