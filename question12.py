def calculate_area(h,b):
    area = 1/2* (h * b)
    return area





height = int(input("Enter height of a triangle"))
base = int(input("Enter base of a triangle"))

area = calculate_area(height,base)
print("Area of triangle is "+str(area)+"square units")