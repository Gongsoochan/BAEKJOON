p, k = map(int,input().split())
lists = []
for i in range(2,k+1):
    if p%i==0:
        lists.append(i)
if len(lists)>0:
    if min(lists)<k:
        print("BAD",min(lists))
    else:
        print("GOOD")
else:
    print("GOOD")
