age = int(input("Enter your age: "))
if age >= 18:
    nationality = input("Enter your nationality is Pakistani: (yes,no)")
    if nationality == "yes":
        print("You are eligible to vote.")
    elif nationality == "no":
        print("Please obtain a valid ID to vote.")
else:
    print("You cannot have an ID card")
