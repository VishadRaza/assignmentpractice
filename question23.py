def celcius_to_fah(c):
    f = (c * 9/5) + 32
    print("Temperature in fahrenheit "+str(round(f,3))+" F")

def fah_to_cel(f):
    c = (f-32) * 5/9
    print("Temperature in celsius " + str(round(c,3)) + " C")


check = int(input("press 1 for entering temperature in celsius and 2 for fahrenheit"))
if check == 1:
    c = float(input("enter temperature"))
    celcius_to_fah(c)
else:
    f = float(input("enter temperature"))
    fah_to_cel(f)