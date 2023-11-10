while True:
    try:
        result = []
        result1 = []
        last = []
        answer = []
        n = list(map(int,input().split()))
        if len(n)==2:
            print("Jolly")
        elif len(n)>2:
            n=n[1:]
            result = n
            for i in range(len(result)-1):
                result1.append(abs(result[i]-result[i+1]))
            r_result1 = set(result1)
            r_result1 = list(r_result1)
            for j in range(1,len(n)):
                last.append(j)
            if r_result1==last:
                print("Jolly")
            else:
                print("Not jolly")
    except EOFError:
        break