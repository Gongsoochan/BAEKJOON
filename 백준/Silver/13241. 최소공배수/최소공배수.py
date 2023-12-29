a,b = map(int,input().split())
n = a*b

while b:
    if a>b:
        a,b = b,a
    b %= a
print(n//a)