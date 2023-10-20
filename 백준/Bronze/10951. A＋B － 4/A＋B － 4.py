a_list=[]

while True:
    try:
        A,B=map(int,input().split())
        a_list.append(A+B)
    except:
        break
for i in a_list:
    print(i)