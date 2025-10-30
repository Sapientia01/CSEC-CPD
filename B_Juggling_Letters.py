from collections import Counter

t  = int(input())
for _ in range(t):
    n = int(input())
    s = ''
    for i in range(n):
        s += input()

    out = "YES"

    s_freq = Counter(s)

    for key in s_freq.keys():
        if s_freq[key] % n != 0:
            out = "NO"
    print(out)    
