n = int(input())
a = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1  
    y -= 1  
    l = y
    r = a[x] - y - 1   
    a[x] = 0   
    if x > 0:
        a[x - 1] += l   
    if x < n - 1:
        a[x + 1] += r  

for b in a:
    print(b)
