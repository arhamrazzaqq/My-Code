username = input("Enter a username:")
username.find(" ")
username.isalpbha()
if len(username) > 12:
    print("Your username can't be more than 12 charahters")
elif not username.find(" ") ==-1:
    print("Your user name can't contain spaces")
elif not username.isalpbha():
    print("Your username can't ve contain numbers")
else:
    print(f"Welcome{username}")

