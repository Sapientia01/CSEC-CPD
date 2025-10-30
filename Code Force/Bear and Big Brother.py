a,b = [int(i) for i in input().split()]
years = 0
ay = a
by = b
while ay <= by:
    ay = ay * 3
    by = by * 2
    years += 1
print(years)
