chess = [1,1,2,2,2,8]
n = input()
nlist = n.split( )
an = []
for i in range(len(chess)):
    an.append(int(chess[i])-int(nlist[i]))
for j in an:
    print(j, end = ' ')