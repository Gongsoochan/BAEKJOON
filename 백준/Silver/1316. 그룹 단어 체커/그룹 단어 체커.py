n = int(input())
count = 0

for i in range(n):
    a = input()
    cal = []
    if len(a)==1:
        count+=1
    else:
        for j in range(len(a)):
            if j==0:
                cal.append(a[0])
            elif j>0:
                if a[j]==a[j-1]:
                    cal.append(a[j])
                    if j==len(a)-1:
                        count+=1
                elif a[j]!=a[j-1]:
                    if a[j] not in cal:
                        if j==len(a)-1:
                            count+=1
                        else:
                            cal.append(a[j])
                    elif a[j] in cal:
                        break
print(count)