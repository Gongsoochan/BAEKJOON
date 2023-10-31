s = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_n = [0 for i in range(len(alpha))]

for i in s:
    if i in alpha:
        for j in range(len(alpha)):
            if alpha[j] == i:
                alpha_n[j] += 1
for n in alpha_n:
    print(n,end=' ')