str1 = input("enter a string ")

s = str1[::-1]
flg =0
for i in range(0,len(s)):
    if s[i] == str1[i]:
        flg = 0
        continue
    else:
        flg = 1
        break
if flg == 0:
    print("The string is palindrome")
else:
    print("The string is not palindrome")