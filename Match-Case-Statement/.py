def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case _:
            return False 

print(is_weekend("Monday"))               