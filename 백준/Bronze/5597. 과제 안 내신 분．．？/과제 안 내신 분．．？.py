c_list = [i for i in range(1, 31)]
for _ in range(28):
    c_list.remove(int(input()))
for i in c_list:
    print(i)