#CREAT GIOMETERY SHAPES
#main input
#_____________________________________________

rows = int(input("Enter nums of rows: "))
coloumns = int(input("Enter nums of coloumns: "))
symbol = input("Enter a symbol to use: ")

#_____________________________________________
#nested loop
#__________________________
for x in range(rows):
 for y in range(coloumns):
    print(symbol, end="")
 print()
#_________________________
 