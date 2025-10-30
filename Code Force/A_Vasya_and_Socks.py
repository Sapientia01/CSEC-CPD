n,m = map(int, input().split())
d = 0
x = m 
a = 2
# print(x)
while n >= 1 :
    n -= 1
    d += 1
    if d == x:
        n += 1
        x = a * m
        a += 1
print(d)







