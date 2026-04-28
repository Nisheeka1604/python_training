a=input("Enter a string: ")
c=0
for i in range(len(a)):
    if a[i]==" " and a[i+1]!=" ":
        c=c+1
print("total words:", c+1)