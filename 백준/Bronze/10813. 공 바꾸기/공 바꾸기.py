n, m = map(int, input().split())
ball_list = []
for _ in range(1, n+1):
    ball_list.append(_)

for _ in range(m):
    i, j = map(int, input().split())
    ball_list[i-1], ball_list[j-1] = ball_list[j-1], ball_list[i-1]

for _ in ball_list:
    print(_, end=' ')
