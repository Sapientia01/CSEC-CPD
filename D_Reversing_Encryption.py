n = int(input())
t = list(input())

divisors = [d for d in range(1, n + 1) if n % d == 0]

for d in divisors:
    t[:d] = reversed(t[:d])

print(''.join(t))