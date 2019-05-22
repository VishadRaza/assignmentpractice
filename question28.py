import math
octal = int(input("enter number in octal"))
dec = 0
remain = octal
i = 0
while remain > 0:
    z = math.pow(8,i)
   # print(z)
    dec += remain % 10 * z
    remain = int(remain/10)
    i = i+1

print("Decimal is ",dec)

