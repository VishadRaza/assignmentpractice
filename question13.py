def checkvalue(num1,num2):
    if num1 == num2 or (num1 - num2) == 5 or (num1 + num2) == 5:
        return True
    return False





num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))

s = checkvalue(num1,num2)
print(s)