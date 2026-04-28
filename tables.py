number = int(input("Enter a number: "))
limit = int(input("Enter table limit: "))

if number % 2 == 0:
    for i in range(1, limit + 1):
        print("{} x {} = {}".format(number, i, number * i))
else:
    for i in range(1, limit + 1):
        print("{} x {} = {}".format(number, i, number * i))