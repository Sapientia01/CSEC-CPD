t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    l = []
    a = []
    o = []
    for _ in range(n):
        x = list(map(int, input().split()))
        x.sort()
        l.append(x)
    for i in range(n):
        a.append(min(l[i]))
    b = sorted(a)   
    for i in b:
        c = a.index(i) 
        c += 1
        o.append(c)
    if n == 1:
        print(1)
    elif m == 1:
        print( " ".join(map(str, o)))
    else:
        s = 0
        ppc = -1
        cc = -1
        for i in range(n*m):
            cs = i%n 
            if i%n == 0:
                cc += 1
            cp = l[o[cs]-1]
            cpc = cp[cc]
            if cpc < ppc:
                print(-1)
                break
            else:
                 s = i 
            ppc = cpc
        if s == (n * m -1):
            print( " ".join(map(str, o)))  