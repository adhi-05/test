age=int(input("Enter your age:"))
if age<18:
    print("not adult")
elif age>=18 and age<=45:
    print("adult")
elif age>=46:
    print("senior citizen")
else:
    print("Wrong value")