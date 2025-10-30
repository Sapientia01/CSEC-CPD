#hiko_chala_ICPC_B
n = int(input())
out = []
for i in range(n):
    l = [int(i) for i in input().split()]
    a = l[0] + l[1]
    b = l[2] - l[1]
    f1 = 0
    f2 = 0
    l.insert(2,a)
    for i in range(3):
        if (l[i] + l[i+1] == l[i+2] ):
            f1 += 1 
    l.pop(2)
    l.insert(2,b)
    for i in range(3):
        if (l[i] + l[i+1] == l[i+2] ):
            f2 += 1 
    f = max(f1,f2)
    out.append(f)
for i in out:
    print(i)