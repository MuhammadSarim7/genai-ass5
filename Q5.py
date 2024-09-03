age = int(input("Enter your age: "))
if age > 0 and age <= 12:
    print("Person with", age, "age is a child")
elif age > 12 and age <= 19:
    print("Person with", age, "age is a teenager")
elif age > 19 and age <= 59:
    print("Person with", age, "age is an adult")
elif age >= 60:
    print("Person with", age, "age is a senior citizen")
else:
    print("Wrong input")
