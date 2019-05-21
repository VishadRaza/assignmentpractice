seconds = int(input("Enter seconds"))

hours = seconds/3600
minutes = seconds/60
day = seconds/ (24*3600)

print("seconds in hours = ",round(hours))
print("seconds in minutes = ",round(minutes))
print("seconds in days = ",round(day))