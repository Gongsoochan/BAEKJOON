# Quadrant
x=int(input())
y=int(input())
-1000<=x<=1000
x!=0
-1000<=y<=1000
y!=0
if x>0:
    if y>0:
        print(1)
    elif y<0:
        print(4)
elif x<0:
    if y>0:
        print(2)
    elif y<0:
        print(3)