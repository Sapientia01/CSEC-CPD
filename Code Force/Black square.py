sl = [int(i) for i in input().split()]
st = input()
c = 0
for i in st:
    x = int(i) -1
    c += sl[x]
print(c)
