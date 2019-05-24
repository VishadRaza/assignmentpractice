first_name = input("enter your first name")
last_name = input("enter your last name")
a = ""
b = ""
# z = first_name[::-1]
# k = last_name[::-1]

for i in range(1,len(first_name)+1):
    a += first_name[len(first_name) - i]

for j in range(1,len(last_name)+1):
    b += last_name[len(first_name) - j]



print("{} {}".format(a,b))