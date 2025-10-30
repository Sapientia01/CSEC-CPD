#hiko_chala_ICPC_B
n, m = map(int, input().split())
l = []
if n % m == 0:
    for i in range(m):
        l.append(n//m)
else:
    for i in range(m):
        l.append(n//m)
    for i in range(m-n%m ,m):
        l[i] += 1
print(*l)