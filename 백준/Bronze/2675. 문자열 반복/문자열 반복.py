t = int(input())

for i in range(t):
    answer = []
    r, s = map(str, input().split())
    r = int(r)
    for j in range(len(s)):
        answer.append(s[j] * r)
    for k in answer:
        print(k, end="")
    print()
