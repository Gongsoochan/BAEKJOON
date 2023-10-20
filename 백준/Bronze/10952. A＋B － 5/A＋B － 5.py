import sys
c = 1
a_list = []
while c:
    A, B = map(int, sys.stdin.readline().split())
    if (A and B) == 0:
        c = 0
    else:
        a_list.append(A+B)
for i in a_list:
    print(i)