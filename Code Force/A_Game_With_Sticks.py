n,m = map(int,input().split())
x = n*m
l = list(range(1, x +1))
s = 0 
while x > 0:
    if  m > n or  n > m :
         x -= -(n+m)
    else:
        x -= -(n+m-1)
    m -= 1
    n -= 1
    s += 1
if s % 2 == 0:
    print("Akshat")
else:
    print("Malvika")