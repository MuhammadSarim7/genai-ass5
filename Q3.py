n = int(input("Enter number: "))
if n % 2 == 0 and n % 3 == 0:
    print(n, "is divisble by both 2 and 3")
elif n % 2 == 0:
    print(n, "is divisble by only 2")
elif n % 3 == 0:
    print(n, "is divisble by only 3")
elif n % 2 != 0 and n % 3 != 0:
    print(n, "is not divisible by both 2 and 3")
else:
    print("Wrong input!")
