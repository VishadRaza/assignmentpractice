import math

def euclidean(x1,y1,x2,y2):
    x = (x2-x1)
    x_sqr =math.pow(x,2)
    y = (y2 - y1)
    y_sqr = math.pow(y, 2)

    result = x_sqr + y_sqr
    res = math.sqrt(result)
    return res


x1 = int(input("input x1"))
x2 = int(input("input x2"))
y1 = int(input("input y1"))
y2 = int(input("input y2"))

result = euclidean(x1,y1,x2,y2)
print(round(result,2))
