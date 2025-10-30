n = int(input())
if n % 2 != 0:
    print(-1)
else:
    out = []
    for i in range(1, n + 1, 2):
        out.append(i + 1)
        out.append(i)
    print(' '.join(map(str, out)))
