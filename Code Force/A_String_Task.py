w = input().lower()
l = []
v = ["a", "o", "y", "e", "u", "i"]
for i in w:
    if i in v:
        continue
    else:
        l.append(i)
o = ''
for i in l:
    o += '.' + i
print(o)
