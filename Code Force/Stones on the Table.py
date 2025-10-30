n = int(input())
stones = input()
t = 0
for i in range(n-1):
    if stones[i] == stones[i+1]:
        t += 1
print(t)
