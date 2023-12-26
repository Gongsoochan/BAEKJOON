n = int(input())
user = []
for i in range(n):
    age, name = input().split()
    user.append([int(age),name])
user = sorted(user, key=lambda x: x[0])

for i in range(n):
    print(user[i][0],user[i][1])