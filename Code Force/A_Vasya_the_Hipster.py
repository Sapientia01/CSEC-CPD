r,b = map(int,input().split())
a = min(r,b)
b = (max(r,b) - a) // 2
print(a,b)