a=int(input("Enter the first name: "))
b=int(input("Enter the second name: "))
l1st=list(a)
l2st=list(b)
for i in l1st:
    if i in l2st:
        l1st.remove(i)
        l2st.remove(i)
l1=len(l1st)
l2=len(l2st)
total=l1+l2
if total%6==0:
    print("Siblings")
elif total%6==1:
    print("Friends")
elif total%6==2:
    print("Love")
elif total%6==3:
    print("Affection")
elif total%6==4:
    print("Marriage")
elif total%6==5:
    print("Enemy")
else:    print("Error")