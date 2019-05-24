st = input("enter string ")
word = input("enter letter fto check its occurrence ")
k=0
for i in range(0,len(st)):
    if st[i] == word:
        k = k + 1
    else:
        continue
print("The number of occurrence of {} is {} ".format(word,k))