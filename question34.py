string = input("enter any text")
vol_count = 0
const_count = 0

for i in range(0,len(string)):
    if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u' :
        vol_count = vol_count + 1
    else:
        const_count += 1

print("The number of occurrence of vowels is {} and the number of occurrence of constants is {}".format(vol_count,const_count))