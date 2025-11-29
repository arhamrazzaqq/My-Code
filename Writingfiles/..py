import json
import csv

# ============================
# 1. Writing to a .txt file
# ============================

text_data = [
    "Hello, this is a text file!",
    "We are writing multiple lines using Python.",
    "This line is also part of the text file."
]

with open("example.txt", "w") as file:
    for line in text_data:
        file.write(line + "\n")


# ============================
# 2. Writing to a .json file
# ============================

json_data = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "skills": ["Python", "Java", "C++"]
}

with open("example.json", "w") as file:
    json.dump(json_data, file, indent=4)


# ============================
# 3. Writing to a .csv file
# ============================

csv_rows = [
    ["Name", "Age", "Country"],
    ["John", 30, "USA"],
    ["Sarah", 25, "Canada"],
    ["Mike", 27, "UK"]
]

with open("example.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_rows)


print("All files created successfully!")
