t= int(input())
for _ in range(t):
    a,b,c,d  = map(int,input().split())
    s1 = max(a,b)
    s2 = max(c,d)
    if s1 > min(c,d) and  s2 > min(a,b):
        print("YES")
    else:
        print("NO")

