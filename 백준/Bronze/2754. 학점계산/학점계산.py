a = input()

if a[0]=='A':
    num = 4.0
elif a[0]=='B':
    num = 3.0
elif a[0]=='C':
    num = 2.0
elif a[0]=='D':
    num = 1.0
elif a[0]=='F':
    num = 0.0

if num>0.0:
    if a[1]=='+':
        result = num + 0.3
    elif a[1]=='-':
        result = num - 0.3
    else:
        result = num
else:
    result = num
print(result)