n = int(input())
for i in range(1,2*n):
    if i<n:
        print(' '*(n-i)+'*'*(2*i-1))
    elif i==n:
        print('*'*(2*i-1))
    elif i>n:
        print(' '*(i-n)+'*'*(2*(n-(i-n))-1))