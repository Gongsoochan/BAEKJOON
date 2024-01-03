n = int(input())
result = []
for i in range(n):
    a = int(input())
    if a != 0:
        result.append(a)
    else:
        result.pop(-1)
print(sum(result))