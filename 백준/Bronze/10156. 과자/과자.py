K,N,M=map(int,input().split())
if K*N<M:
    print(0)
elif K*N>=M:
    print(int(K*N-M))