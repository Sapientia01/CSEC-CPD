t = int(input())
for i in range(t):
    x = int(input())
    i = 2
    l = []
    f = []
    while i <= x//5:
        if x%i == 0:
            l.append(i)
        i += 1
    if len(l) < 3:
        print("NO") 
    else:
        for a in l:
            if len(f)>0:
                break    
            for b in l:
                 if x / (a *b) in l:
                     p = []
                     p.append(a)
                     p.append(b)
                     p.append(x/(a*b))
                     f.append(p)
                     break 
        print("YES")
        p = map(int, f[0])
        print(" ".join(map(str, p)))