#WHILE LOOP AND IF ELSE STATEMENT
while True:
  username = input("Enter your name: ")

  if username.isalpha() and username.isdigit():
    print("Your name is: ")
    break
  else:
    print("Your username can only contain letters and digits")