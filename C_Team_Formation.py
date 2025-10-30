n = int(input())
skills = list(map(int,input().split()))
skills.sort()
problems = 0

for i in range(0,n,2):
    first = skills[i]
    second = skills[i+1]
    problems += abs(first-second)
print(problems)