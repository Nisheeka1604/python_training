import random
p1=input("Enter player 1 name: ")
p2=input("Enter player 2 name: ")  
s1=10
s2=10
d1=random.randint(1,10)
d2=random.randint(1,10)
print("________________player1 turn________________")
while(True):
    g1=int(input("enter your guess"))
    s1=s1-1
    if g1==d1:
        break
print("________________player2 turn________________")
while(True):
    g2=int(input("enter your guess"))
    s2=s2-1
    if g2==d2:
        break
print("summary")
print("{}:{}".format(p1, s1))
print("{}:{}".format(p2, s2))
if s1>s2:
    print("player1 is winner")
else:
   print("player2 is winner")