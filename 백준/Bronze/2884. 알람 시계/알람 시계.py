H,M=map(int,input().split())
0<=H<=23
0<=M<=59
if (M-45)<0:
  if (H-1)<0:
    print(f"{24+(H-1)} {60+(M-45)}")
  elif (H-1)>=0:
    print(f"{H-1} {60+(M-45)}")
elif (M-45)>=0:
  print(f"{H} {M-45}")