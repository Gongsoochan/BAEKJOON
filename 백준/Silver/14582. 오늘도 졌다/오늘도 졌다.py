myteam = 0
enemy = 0
inning = 9
result = []
myteam_score = list(map(int,input().split()))
enemy_score = list(map(int,input().split()))

for i in range(inning):
    if i > 0:
        myteam_score[i] = myteam_score[i-1] + myteam_score[i]
        enemy_score[i] = enemy_score[i-1] + enemy_score[i]
    if i == 0 and myteam_score[i] > 0:
        result.append('win')
    elif i > 0 and myteam_score[i] > enemy_score[i-1]:
        result.append('win')
    else:
        result.append('lose')
if myteam_score[-1] < enemy_score[-1]:
    result.append('lose')
if 'win' in result:
    if myteam_score[-1] < enemy_score[-1]:
        print("Yes")
else:
    print("No")
