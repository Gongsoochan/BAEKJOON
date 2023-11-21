def de(x,y):
    if x/y>x//y:
        return x//y+1
    else:
        return x//y

nlist = []
l = int(input())

for i in range(4):
    n = int(input())
    nlist.append(n)

a = de(nlist[0],nlist[2])
b = de(nlist[1],nlist[3])

if a>b:
    print(l-a)
else:
    print(l-b)