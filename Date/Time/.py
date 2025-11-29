import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
time_now = datetime.datetime.now()

now = time_now.strftime("%H:%M:%S %m-%d-%Y")
target_datetime = datetime.datetime(2030, 1, 2, 3, 4, 5)
current_datetime = datetime.datetime.now()
if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has passed")