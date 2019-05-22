import numpy
num = int(input("Enter a number"))
o = num
h = num
#Binary conversion
s = ""

for i in range(0,8):
    if num % 2 == 1:
        s = '1' + s

    elif num % 2 == 0:
        s = '0' + s

    num = int(num / 2)


print("Its binary equivalent is  ", s)

#Octal conversion
q = 0
oct_num = []
temp = o
while temp != 0:
    m = temp % 8
    oct_num.append(m)
    temp = int(temp / 8)
    q = q + 1

st = oct_num[::-1]
res = int("".join(map(str, st)))
print("octal equivalent is ", res)

#Hexadecimal conversion
w = 0
hex_num = ""
mem = h
while mem != 0:
    u = mem % 16
    hexchar = ""
    if u <= 9 and u >= 0:
        hexchar = u
    elif u == 10:
        hexchar = 'A' + hexchar
    elif u == 11:
        hexchar = 'B' + hexchar
    elif u == 12:
        hexchar = 'C' + hexchar
    elif u == 13:
        hexchar = 'D' + hexchar
    elif u == 14:
        hexchar = 'E' + hexchar
    elif u == 15:
        hexchar = 'F' + hexchar
    hex_num = str(hexchar) + hex_num
    mem = int(mem / 16)

print("The hexadecimal equivalent is ",hex_num)





