legs=int(input("Enter the number of legs: "))
heads=int(input("Enter the number of heads: "))
flag=False
for cows in range(0,heads+1):
    hens=heads-cows
    cal_legs=4*cows+2*hens
    if cal_legs==legs:
        flag=True
        print("number of cows:", cows)
        print("number of hens:", hens)
        break
if flag:
    print("cows:", cows)
    print("hens:", hens)
else:    print("no solution")