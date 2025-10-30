from collections import defaultdict

n, k = map(int, input().split())
s = input().strip()

remove_count = defaultdict(int)
for c in range(26):
    ch = chr(ord('a') + c)
    for i in range(len(s)):
        if s[i] == ch:
            remove_count[ch] += 1
            k -= 1
            if k == 0:
                break
    if k == 0:
        break
result = []
for ch in s:
    if remove_count[ch]:
        remove_count[ch] -= 1
    else:
        result.append(ch)

print( ''.join(result))
