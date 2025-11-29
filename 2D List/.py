groceries=[("Apple", "Banana", "Cherry"),
            ("Carrot", "Broccoli", "Spinach"),
            ("chicken", "beef", "fish")]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()


print(groceries[0][2])