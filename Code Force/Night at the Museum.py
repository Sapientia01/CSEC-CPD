s = input()
p = ord("a")
r = 0
for i in range(len(s)):
    x = abs(p - ord(s[i]))
    p = ord(s[i])
    if x > 13:
        r += (26-x)
    else:
        r += x
print(r)
