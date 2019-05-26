n = int(input("enter a number "))

for i in range(n):
    for j in range(0,i):
        print("*", end="")
    print()


for k in range(n,0,-1):
    for l in range(0,k):
        print("*", end="")
    print()



