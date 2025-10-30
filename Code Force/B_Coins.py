comparition = []
for i in range(3):
    l =  list(input())
    comparition.append(l)
weights = ["A","B","C"]
large = []
wins = []
for i in comparition:
    if i[1] == ">" :
        large.append(i[0])
    else:
        large.append(i[2])
w = list(set(large))
for i in  w:
    win = []
    win.append(large.count(i))
    win.append(i)
    wins.append(win)
wins.sort()
order = ''
if wins[0][0]+1 != wins[1][0]:
    print("Impossible")
else:
    for i in weights:
        if i not in large:
            order = i
    for i in wins:
        order += i[1]
    print(order)