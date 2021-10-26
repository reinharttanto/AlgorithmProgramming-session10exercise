

def convert_to_days():
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))
    x = minutes + (seconds / 60)
    y = hours + (x / 60)
    days = round(y / 24, 4)
    print("The number of days is:", days)


convert_to_days()