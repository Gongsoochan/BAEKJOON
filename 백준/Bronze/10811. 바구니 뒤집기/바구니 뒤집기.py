n, m = map(int, input().split())
basket_list = []
for i in range(1, n+1):
    basket_list.append(i)
for _ in range(m):
    i, j = map(int, input().split())
    basket_list[i-1:j-1],basket_list[j-1:i-1:-1]=basket_list[j-1:i-1:-1],basket_list[i-1:j-1]
for k in basket_list:
    print(k,end=' ')
