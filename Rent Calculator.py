# Rent calculator program by DJ
Flat  = int(input("Enter your flat Rent : "))
food = int(input("Enter your total Food Expendure : "))
electricity  = int(input("Bill of the electricity uses : "))
wifi = int(input("Enter your wifi bill"))

student = int(input("Enter the number of student "))

total = Flat+food+electricity+wifi
per_person = total/student
print(f"Your Total Expendure of month is {total}")
print("------------------------------------")
print(f"your total Per person amount is {per_person}")f