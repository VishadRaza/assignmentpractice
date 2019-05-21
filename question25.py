num = []
num = input("Enter number")


n = str(num)
z = n[0:]
x =len(z)
sum = 0
for i in range(0,x):
    print(num[i])
    s = int(num[i])
    sum = sum + s

print("Sum is ",sum)

