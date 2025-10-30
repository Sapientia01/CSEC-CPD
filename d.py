t  = int(input())
for i in range(t):
    n,k,p = list(map(int, input().split()))
    a = 0
    sa = 0
    if abs(k) > (n*p):
        print(-1) 
    else:
        x = abs(k)// p
        if abs(k) % p == 0:
            print(x)
        else:
            print(x+1)
