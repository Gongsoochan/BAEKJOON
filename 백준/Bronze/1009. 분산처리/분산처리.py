a1 = [1]
a2 = [2, 4, 8, 6]
a3 = [3, 9, 7, 1]
a4 = [4, 6]
a5 = [5]
a6 = [6]
a7 = [7, 9, 3, 1]
a8 = [8, 4, 2, 6]
a9 = [9, 1]
a10 = [0]
a_list = [a10, a1, a2, a3, a4, a5, a6, a7, a8, a9]
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    a_re = a % 10
    a_result = a_list[a_re]
    result = a_result[b % len(a_result)-1]
    if result == 0:
        print(10)
    else:
        print(result)
