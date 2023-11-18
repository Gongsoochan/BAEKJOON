n, m = map(int,input().split())
al = [[0] * m for i in range(n)]
bl = [[0] * m for i in range(n)]
an = [[0] * m for i in range(n)]

for i in range(n):
    a = list(map(int,input().split()))
    for j in range(m):
        al[i][j] = a[j]

for i in range(n):
    b = list(map(int,input().split()))
    for j in range(m):
        bl[i][j] = b[j]

for i in range(n):
    for j in range(m):
        an[i][j] = al[i][j] + bl[i][j]
    print(*an[i])