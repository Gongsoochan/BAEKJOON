A,B=map(int,input().split())
C=int(input())
0<=A<=23
0<=B<=59
0<=C<=1000
a=(B+C)//60
b=(B+C)%60
if B+C<60:
    print(A,B+C)
elif B+C>=60:
    if A+a>=24:
        print((A+a)-24,b)
    elif A+a<24:
        print(A+a,b)