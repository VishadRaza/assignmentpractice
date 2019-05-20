import math

def hypotenuse_calculate(a,b):
    c = (a*a) + (b*b)
    hyp = math.sqrt(c)
    return hyp

a = float(input("enter base"))
b = float(input("enter height"))
result = hypotenuse_calculate(a,b)
print(round(result,1))