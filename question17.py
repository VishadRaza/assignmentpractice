height = input("input height in feet and inches")

s = height.split(',')
feet = int(s[0])
inch = int(s[1])

inches = feet * 12

total_inches = inches + inch

total_height = total_inches * 2.54
print("Height in centimeter "+str(round(total_height,1))+" cm")
