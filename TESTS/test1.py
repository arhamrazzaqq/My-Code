#SIMPLE CALCULATOR PROGRAM
program = input("Enter a sign to use(/ * + - ): ")


number0 = int(input("Enter a number:  "))
number1 = int(input("Enter another number: "))


if program == "/":
    result = number0 / number1
    print(result)
elif program == "*":
    result = number0 * number1
    print(result)
elif program == "+":
    result = number0 + number1
    print(result)
elif program == "-":
    result =number0 - number1
    print(result)
else:
     print("InValid Input!")