l=[15,2,7,25,10]
"""mini=l[0]
maxi=l[0]
for i in range(0,len(l)):
    if l[i]<mini:
        mini=l[i]
    if l[i]>maxi:
        maxi=l[i]
print("Minimum value is:", mini)
print("Maximum value is:", maxi) """

l.sort()
print("Minimum value is:", l[0])
print("Maximum value is:", l[len(l)-1])