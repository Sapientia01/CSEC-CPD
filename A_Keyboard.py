keys = "qwertyuiopasdfghjkl;zxcvbnm,./"
o = input().upper()
word = input()
out = []
if o == 'R':
    for i in word:
        x = keys.index(i) -1
        out.append(keys[x])
elif o == "L":
     for i in word:
        x = keys.index(i) + 1
        out.append(keys[x])
print("".join(map(str,out)))
