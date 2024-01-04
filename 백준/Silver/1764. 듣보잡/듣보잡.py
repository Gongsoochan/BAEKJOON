h, s = map(int,input().split())
not_heard = set()
not_seen = set()
result = []

for _ in range(h):
    not_heard.add(input())
for _ in range(s):
    not_seen.add(input())
for i in not_heard:
    if i in not_seen:
        result.append(i)

result.sort()
print(len(result))
print('\n'.join(result))