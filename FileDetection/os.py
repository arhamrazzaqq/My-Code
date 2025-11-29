import os

file_path = "C:/Users/Arham/Desktop/test"

if os.path.exists(file_path):
    print(f"The Loctaion {file_path} Exists")

    if os.path.isfile(file_path):
        print("That Is A File")
    elif os.path.isdir(file_path):
        print("That Is A Directory")

else:
    print("That Location Doesn't Exist")
