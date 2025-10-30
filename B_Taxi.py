n= int(input())
l = list(map(int, input().split()))
l.sort()
t = 0
while 4 in l:
        t += 1
        l.remove(4)        
for x in l:
    for y in l:
      if x + y == 4:
            t += 1
            l.remove(x)
            l.remove(y)
            



print(l)
print(t)
          