a, b, c = map(int,input().split())
n = []
n.append(a)
n.append(b)
n.append(c)
n.sort()
for i in n:
    print(i, end=' ')