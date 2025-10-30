t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    min_op = 0

    left = 0
    right = 0
    while left < n :
        while left < n and s[left] == "W":
            left += 1
        if left < n:
            min_op += 1
            left += k
        
    print(min_op)
