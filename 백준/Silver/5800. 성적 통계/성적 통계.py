k = int(input())
for i in range(k):
    Largest_gap = []
    n = list(map(int,input().split()))
    n = n[1:]
    n.sort()
    print("Class",i+1)
    for j in range(len(n)):
        if j+1<len(n):
            Largest_gap.append(n[j+1]-n[j])
    print(f"Max {max(n)}, Min {min(n)}, Largest gap {max(Largest_gap)}")