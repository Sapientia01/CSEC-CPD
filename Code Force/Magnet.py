n = int(input())
l = []
for i in range(n):
    l.append(input())
g = 1
for i in range(n-1):
    if l[i] != l[i+1]:
        g += 1
print(g)
