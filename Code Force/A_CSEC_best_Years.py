year = input()
year = str(int(year)+1)
while len(set(year)) != len(year):
    year = str(int(year)+1)
print(year)
