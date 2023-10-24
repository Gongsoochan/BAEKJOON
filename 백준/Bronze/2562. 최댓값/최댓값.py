n_list = []
for i in range(9):
    n = int(input())
    n_list.append(n)
max_n = max(n_list)
print(max_n)
print(n_list.index(max_n)+1)
