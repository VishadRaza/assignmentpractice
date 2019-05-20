def checkstring(str):
    if str[:2] == "is":
        return str
    return "Is" + str



str = input("Enter a string")

s = checkstring(str)
print("The returned string is ",s)
