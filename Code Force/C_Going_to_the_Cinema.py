t = int(input())
for _ in range(t):
    n = int(input())
    l = sorted(list(map(int,input().split())))
    p = 1
    if l[0] != 0:
        p -= 1
    for i in range(n-1):
        if l[i] <= i and l[i+1] > i+1:
            p += 1

    if len(l) == 2 and sum(l) == 2:
        p = 2
    if l[-1] == 0:
        p +=n    
    print(p)