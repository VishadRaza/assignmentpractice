import math

radius = float(input("input radius of sphere"))

volume = (4/3) * math.pi * math.pow(radius,3)
vol = round(volume,3)
print("volume of sphere is ",vol)