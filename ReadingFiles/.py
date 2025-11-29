import json
import csv

#.txt
#______________________________________________________
file_path = "C:/Users/Arham/Desktop/notes.text"
try:
   with open(file_path, "r") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("You don't have permission to read the file")
#______________________________________________________

#.json
#______________________________________________________
file_path = "C:/Users/Arham/Desktop/notes.json"
try:
   with open(file_path, "r") as file:
    content = json.load(file)
    print(content)
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("You don't have permission to read the file")
#______________________________________________________

#.csv
#
file_path = "C:/Users/Arham/Desktop/notes.csv"
try:
   with open(file_path, "r") as file:
    content = csv.reader(file)
    for row in content:
       print(row)
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("You don't have permission to read the file")
#______________________________________________________

