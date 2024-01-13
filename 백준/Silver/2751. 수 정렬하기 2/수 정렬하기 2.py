import sys
n = int(sys.stdin.readline())
test = []
for _ in range(n):
    num = int(sys.stdin.readline())
    test.append(num)
test.sort()
for i in test:
    print(i)