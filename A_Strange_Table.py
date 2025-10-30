t = int(input())

for _ in range(t):
    n,m,x = map(int,input().split())
    
    col = x//n

    if x/n > col:
        col += 1

    row = x - ((col-1) * n)

    res = m * (row-1) + col

    print(res)
    