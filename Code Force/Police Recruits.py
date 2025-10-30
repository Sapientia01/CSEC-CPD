n =  int(input())
h = [int(i) for i in input().split()]
p = 0
c = 0
for i in h:
    if i < 0 and p <= 0 :
        c -= (-i)
    elif i < 0 and p > 0:
        p -= (-i)
        if p < 0:
            c -= (-p)
            p = 0
    elif i > 0:
        p += i
print(-c)
