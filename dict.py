a=input("Enter a name: ")
b=int(input("Enter age: "))
c=input("Enter city: ")

dict={}
dict["name"]=a
dict["age"]=b  
dict["city"]=c

#update dict["name"]="nishi"

for i,j in dict.items():
    print(i,j)

print(dict)