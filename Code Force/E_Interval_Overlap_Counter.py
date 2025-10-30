n = int(input())
start = []
end = []
all_e = []
one = 0
two = 0 
three = 0
for i in range(n):
    a,b = map(input().split())
    start.append(a)
    end.append(b)
    all_e.append(a)
    all_e.append(b)

ends = set(all_e)
three += len(ends) //3


