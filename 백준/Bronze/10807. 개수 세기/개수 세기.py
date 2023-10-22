N = int(input())
l = list(map(int, input().split()))
v = int(input())
if N == len(l):
    print(l.count(v))