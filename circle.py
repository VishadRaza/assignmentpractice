import math

radius = float(input("enter radius of circle"))

area = math.pi * math.pow(radius,2)
r = round(area,3)

print("Area of a circle is  "+str(r))