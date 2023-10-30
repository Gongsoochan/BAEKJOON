a = int(input())
score_l = []
score = list(map(int, input().split()))
m = (max(score))
for i in (score):
    b = i/m * 100
    score_l.append(b)
aver = 0
for j in score_l:
    aver += j
print(aver/len(score))
