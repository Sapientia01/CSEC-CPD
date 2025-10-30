cards = int(input())
numbers = [int(i) for i in input().split()]
s = 0
d = 0
for i in range(cards):
    l = [numbers[0],numbers[-1]]
    x = max(l)
    if i % 2 == 0:
        s += x
    else:
        d += x
    numbers.remove(x)
    l.clear()
print(s,d)
