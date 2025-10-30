order= input()
instruction = input()
p = 0
for i in instruction:
  if order[p] == i:
    p += 1
print(p+1) 