alpha = input()
alpha_u = alpha.upper()
alpha_u = sorted(alpha_u)
answer = []
alpha_us = set(alpha_u)
alpha_us = sorted(alpha_us)

for i in alpha_us:
    ca = alpha_u.count(i)
    answer.append(ca)

an = answer[:]
answer.sort()

if len(answer)==1:
    print(alpha_us[0])
elif len(answer)>1:
    if answer[-1]==answer[-2]:
        print("?")
    elif answer[-1]!=answer[-2]:
        print(alpha_us[an.index(max(answer))])
