s = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = [-1] * len(alpha)
for i in range(len(s)):
    for j in range(len(alpha)):
        if s[i] == alpha[j]:
            if answer[j] > -1:
                pass
            elif answer[j] == -1:
                answer[j] = i
for k in answer:
    print(k, end=' ')
