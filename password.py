a=input("enter a password: ")
up=0
low=0
special=0
dg=0
if len(a)>7:
    for i in a:
        if i.isupper():
            up=up+1
        elif i.islower():
            low=low+1
        elif i.isdigit():
            dg=dg+1
        else:
            special=special+1
else:    print("password should be more than 8 characters")
if up>0 and low>0 and special>0 and dg>0:
    print("strong password")
else:
    print("weak password")