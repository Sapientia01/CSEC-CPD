r,c = map(int,input().split())
drawing = []
turn = "r"
for i in range(r):
    if i %2 == 0:
        line = "#" * c
        drawing.append(line)
    else: 
        if turn == "r":
            line = "." * (c-1) + "#" 
            turn = "l"
        else:
            line = "#" +  "." * (c-1) 
            turn = "r"
        drawing.append(line)
for line in drawing:
    print(line)



