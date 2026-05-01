a=input().split(",")
l=(int(item) for item in a)
n=(int(input("Enter a number to count: ")))
#c=0
#for i in l:
 #   if i==n:
  #      c+=1
#print("count of {} is: {}".format(n,c))
c=l.count(n)
print(c)
    
                    