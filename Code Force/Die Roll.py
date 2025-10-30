y,w = [int(i) for i in input().split()]
p = 6 - max(y, w) + 1
def d(a, b):
    while b:
      a, b = b, a % b
    return a
c = d(p,6)
print(f"{p // c}/{6 // c}")
