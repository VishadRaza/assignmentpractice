def square(num):
    z = num * num
    return z
def thrice(num):
    y = num * num * num
    return y


num = int(input("Enter a number"))
z = square(num)
y = thrice(num)
n = num + z + y

print(n)



