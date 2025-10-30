n,h = [int(i) for i in input().split()]
hn = [int(i) for i in input().split()]
width = 0
for i in hn:
    if i>h:
        if i/h > i//h:
            width += i//h + 1
        else:
             width += i//h
    else:
          width += 1
print(width)