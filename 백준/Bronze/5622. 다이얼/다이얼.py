num = input()
alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
an = []
for i in num:
    for j in range(len(alpha)):
        if i in alpha[j]:
            an.append(j+3)
print(sum(an))