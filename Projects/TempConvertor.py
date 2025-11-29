unit = input("Celsius or Farenheit (C/F); ")
temp = float(input("Enter The Temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"The Temperature Is In Fahrenhiet Is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2) 
    print(f"The Temperature In Celcius Is: {temp}°C")
else:
    print(f"{unit} is an unvalid unit of measurement")
