hours = int(input("input time in hours: "))
minutes = int(input("input time in minutes: "))

hr_sec = hours * 3600
min_sec = minutes * 60

sec = round(hr_sec+min_sec)

print("Time in seconds ",sec)