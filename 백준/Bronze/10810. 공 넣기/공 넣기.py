n, m = map(int, input().split())
n_list = []

for _ in range(1, n+1):
    n_list.append(0)

for _ in range(m):
    i, j, k = map(int, input().split())
    if j >= i:
        for _ in range(j-i+1):
            n_list[i-1] = k
            i += 1

for _ in n_list:
    print(_, end=' ')
