n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    d =  b-a
    if d == 0:
        print(0)
    elif d > 0 and d % 2 == 1:
        print(1)
    elif d > 0 and d %2 ==0:
        print(2)
    elif d < 0 and abs(d) % 2 == 0:
        print(1)
    elif d < 0 and abs(d) % 2 == 1:
        print(2)