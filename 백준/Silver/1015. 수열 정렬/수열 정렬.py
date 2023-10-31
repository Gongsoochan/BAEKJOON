n = int(input())
a = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    idx = a.index(min(a))
    answer[idx] = i
    a[idx] = 9999

for j in answer:
    print(j, end=' ')
