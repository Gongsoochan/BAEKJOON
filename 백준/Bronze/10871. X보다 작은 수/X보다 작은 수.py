N, X = map(int, input().split())
A = list(map(int, input().split()))
answer_list = []
for i in A:
    if i < X:
        answer_list.append(i)
print(' '.join(map(str, answer_list)))
