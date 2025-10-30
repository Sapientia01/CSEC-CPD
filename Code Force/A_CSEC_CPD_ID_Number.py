#hiko_chala_ICPC_B
n = int(input())
out = []
for i in range(n):
    l = list(input())
    f = 0
    s = 0
    for i in range(len(l)):
        x = int(l[i])
        if i < 3:
            f += x
        else:
            s += x
    if f == s:
        out.append("YES")
    else:
        out.append("NO")
for i in out:
    print(i)