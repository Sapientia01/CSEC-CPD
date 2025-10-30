
def try_char(s, c):
    l, r = 0, len(s) - 1
    removals = 0
    while l < r :
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] == c:
            l += 1
            removals += 1
        elif s[r] == c:
            r -= 1
            removals += 1
        else:
            return float('inf')
        
    return removals

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    ans = float('inf')
    for c in "abcdefghijklmnopqrstuvwxyz":
        ans = min(ans, try_char(s, c))

    print(-1 if ans == float('inf') else ans)