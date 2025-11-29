temp  = 238
is_sunny = True

if temp > 28 and is_sunny:
    print("It Is Hot OutSide!!!")
    print("It Is Sunny!!")
elif temp <= 0 and is_sunny:
    print("It Is Cold OutSide!!!")
    print("It Is Sunny")
elif 28 > temp > 0 and is_sunny:
    print("It Is Warm OutSide")
    print("It Is Sunny")

    temp = 36
is_raining = True

if temp > 35 or temp < 0 and not is_raining: 
    print("The Party Is Cancelled")
else:  
    print("The Party Is STILL UP")