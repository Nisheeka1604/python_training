#10,20,30,40,50,10,20,30,40,50
a=input().split(",")
l=[int(item) for item in a]
"""newl=[]
for i in l:
    if i in newl:
        continue
    else:
        newl.append(i)

print(newl)
 """

s=set(l)
s=sorted(s)
newl=list(s)
print(newl)