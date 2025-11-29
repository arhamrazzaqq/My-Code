import time
my_time = int(input("Enter Time IN Seconds: "))
for x in range(0 , my_time):
 seconds = x %60
 minutes = int(x /60)%60
 hours = int(x /3600)

 print(f"{hours:02}:{minutes:02}:{seconds:02}")
 time.sleep(1)

print("Bell ringing in...") 