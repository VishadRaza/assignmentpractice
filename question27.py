binary = input("enter binary number ")

s = []
m = 0
k = 0
for i in reversed(range(0, len(binary))):
    b = int(binary[i])
    s = (b * pow(2, k))
    m = m + s
    k = k + 1

print(m)
