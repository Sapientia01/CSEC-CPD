from collections import defaultdict

s = input()
ans = float("inf")
position = defaultdict(list)
for i in range(len(s)):
    position[s[i]].append(i)
for char in position:
    pos = position[char]
    max_gap = 0
    max_gap = max(max_gap, pos[0] + 1)
    for i in range(1, len(pos)):
        max_gap = max(max_gap, pos[i] - pos[i - 1])
    max_gap = max(max_gap, len(s) - pos[-1])
    ans = min(ans, max_gap)
print(ans)