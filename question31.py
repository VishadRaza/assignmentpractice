def gcd(num1,num2):
    while num2:
     if num1 == 0:
        return num2
     elif num2 == 0:
        return num1
     else:
        rem = num1 % num2
        num1 = num2
        num2 = rem
        return num2




num1 = int(input("enter first number "))
num2 = int(input("enter second number "))
k = gcd(num1,num2)
print("GCD is ",k)

