#NEW YEAR CLOCK(KINDOFFFF)
#________________________________________


#Importing datetime module to access os date and time
#_________________________________________
import datetime
#_________________________________________
#Date, today and time
#______________________________________
date = datetime.date(2025, 12, 12)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
time_now = datetime.datetime.now()
#______________________________________
#how to write date and time of today and target time
#______________________________________________
now = time_now.strftime("%H:%M:%S %m-%d-%Y")
target = datetime.datetime(2026, 1, 2, 3, 4, 5)
time_now1 = datetime.datetime.now()
target = time_now1
#______________________________________________
#if else statement
#______________________________________________
if target > time_now1:
    print("HAPPY NEW YEAR!!!!")
else:
    print("NOT YET")
#______________________________________________


