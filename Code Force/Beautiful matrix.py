lines = []
for i in range(5):
 line = [int(i) for i in input().split()]
 lines.append(line)
for i in lines:
 if sum(i)==1:
  y = lines.index(i)+1
x = lines[y-1].index(1)+1
if x >=3 and y>=3:
 x -= 3
 y -=3
elif x<=3 and y<=3:
 x = 3-x
 y = 3-y
elif x>=3 and y<=3:
 x -= 3
 y = 3-y
else:
 y -= 3
 x = 3-x
print(x+y)
