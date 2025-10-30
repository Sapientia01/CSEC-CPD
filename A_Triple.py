t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    if len(l) < 3:
        print(-1)
    else:
        x = max(l)
        nl = [0]*(x +1)
        ft = ' '
        for i in l:
            nl[i] +=1
        for i in range(x+1):
            if nl[i] > 2:
                ft = i
                break
        if ft == ' ':
            print(-1)
        else:
            print(ft)