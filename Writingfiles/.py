import json
import csv

employees = [["Nmae, Age, Job"],
            ["SpongeBob", 30, "Cook"],
            ["Patrick", 37, "Unemployed"],
            ["Sandy", 27, "Scientist"]]

file_path = "C:/Users/Arham/Desktop/notes.csv"
#'a' for append a file
#'r' is to read a file
#'w' is to write a file
#'x' to wite a file if it doesn't exists 

#--------------------------------
#w
try:
    with open(file_path, "w", newline="") as file:
       writer = csv.writer(file)
       for row in employees:
           writer.writerow(row)
       #json.dump(employee, file, indent=2)
       # for employee in employees:
       #   file.write(employee + "\n")
       #print(f"txt file '{file_path}' was created")
       print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That File Already Exists!")