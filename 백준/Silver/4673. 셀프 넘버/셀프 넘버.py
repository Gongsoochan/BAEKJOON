all_num = set(range(1,10001))

for i in range(len(all_num)):
    a = i//10000
    b = (i%10000)//1000
    c = (i%1000)//100
    d = (i%100)//10
    e = (i%10)//1
    ai = i+a+b+c+d+e
    if ai in all_num:
        all_num.remove(ai)
for i in all_num:
    print(i)