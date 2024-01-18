n = int(input())
box = []

for i in range(n):
    box.append(list(map(int,input().split())))

box.sort()

for i in range(n):
    print(box[i][0],box[i][1])