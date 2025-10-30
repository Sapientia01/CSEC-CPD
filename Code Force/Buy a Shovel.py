k,r = [int(i) for i in input().split()]
b = 1
while not(k * b % 10 == 0 or (k * b - r) % 10 == 0):
    b += 1
print(b)
