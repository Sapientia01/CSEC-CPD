from bisect import bisect_right

mod = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    ans = 1
    for i in range(len(b)):
        el = b[i]
        index = bisect_right(a, el)
        if len(a) - index - i <= 0:
            print(0)
            break
        ans *= len(a) - index - i
        ans %= mod
    else:
        print(ans % (mod))