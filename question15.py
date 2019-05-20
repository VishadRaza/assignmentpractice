amount = int(input("Enter amount"))
interst = float(input("Enter interest"))
year = int(input("Enter years"))

future_value = amount*((1+(0.01*interst)) ** year)

print("Future value will be ",round(future_value,2))