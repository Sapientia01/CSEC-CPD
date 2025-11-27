n = int(input())
stones = list(map(int,input().split()))
sorted_stones = sorted(stones)
one_sum = 0
two_sum = 0
one = [0 for i in range(n+1)]
two = [0 for i in range(n+1)]

for i in range(n):
    one_sum += stones[i]
    two_sum += sorted_stones[i]

    one[i+1] = one_sum
    two[i+1] = two_sum

t = int(input())
for _ in range(t):
    t, l, r = map(int,input().split())
    if t == 1:
        print(one[r] - one[l-1] )
    elif t == 2:
        print(two[r] - two[l-1] )