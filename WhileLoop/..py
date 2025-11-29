age = int(input("Enter your age:"))

while age <= 0:
    print("Your age can not be negative or zero!")
    age = int(input("Enter your age;"))

if age == 4:
    print("YOU ARE THE YOUNGEST PERSON EVER!")
else:
    print(f"You are {age} years old!")

