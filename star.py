s=int(input("Enter the number of stars: "))
l=int(input("Enter the number of lines: "))
b=int(input("enter number of boxes: "))
for i in range(s):
    for j in range(l):
        for k in range(b):
            print("*", end="")