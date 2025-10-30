#hiko_chala_ICPC_B
n = int(input())
out = []
c = n + 1
y = list(range(c))
for i in range(n):
    l = []
    a = n - i 
    b = i + 1
    x = list(range(b))
    for j in range(a):
        l.append(' ')
    l.extend(x)
    x.reverse()
    x.pop(0)
    l.extend(x)
    out.append(l)
d = y.copy()
d.reverse()
d.pop(0)
y.extend(d)
out.append(y)
for i in range(n):
    a = n- 1-i
    x = out[a]
    out.append(x)   

for i in out:
    print(*i)
