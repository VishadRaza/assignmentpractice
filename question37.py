def rev_number(n):
  s = 0
  while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n += m
      s += 1
  return n

n = int(input("enter a number "))
z = rev_number(n)
x = str(z)
if x[0:] == x[::-1]:
    print("{} is a palindrome".format(x))
else:
    print("{} is a not palindrome".format(x))