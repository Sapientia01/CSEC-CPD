from bisect import bisect_left, bisect_right

t = int(input())
for _ in range(t):
    n,x,y = map(int, input().split())  
    a = list(map(int, input().split()))
    totalSum = sum(a)
    lower = totalSum - y
    upper = totalSum - x
    a.sort()
    pairs = 0
    for i in range(n):
        low = lower - a[i]
        high = upper - a[i]
        left = bisect_left(a, low, i + 1)
        right = bisect_right(a, high, i + 1)
        pairs += right - left
    print(pairs)
 