n = list(input())
n.sort()
test = []
for i in n:
    test.insert(0,i)
result = ''.join(test)
print(result)