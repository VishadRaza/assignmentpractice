amount = int(input("enter your amount "))
while amount >= 1000:
    a = amount / 1000
    amount = amount % 1000
    print("The no of 1000 notes are ",round(a,0))
    break
while amount >= 500:
    b = amount / 500
    amount = amount % 500
    print("The no of 500 notes are ",round(b,0))
    break
while amount >= 100:
    c = amount / 100
    amount = amount % 100
    print("The no of 100 notes are ",round(c,0))
    break
while amount >= 50:
    d = amount / 50
    amount = amount % 50
    print("The no of 50 notes are ",round(d,0))
    break
while amount >= 20:
    e = amount / 20
    amount = amount % 20
    print("The no of 20 notes are ",round(e,0))
    break
while amount >= 10:
    f = amount / 10
    amount = amount % 10
    print("The no of 10 notes are ",round(f,0))