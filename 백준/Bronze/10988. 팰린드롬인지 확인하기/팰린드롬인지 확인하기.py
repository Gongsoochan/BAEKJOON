s = input()
result = []
for i in range(len(s)):
    if s[i]==s[-i-1]:
        result.append(1)
    else:
        result.append(0)
print(min(result))