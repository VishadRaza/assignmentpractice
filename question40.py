import re
string = input("enter any string ")
d = 0
l = 0
for i in string:
    if i.isdigit():
        d = d + 1
    elif i.isalpha():
        l = l + 1

print("digit count ",d)
print("letter count ",l)


