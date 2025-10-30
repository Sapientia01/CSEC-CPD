y = input()
x = int(y)
d = 0
for i in y:
    if i == '4' or i == '7':
        d += 1
if x > 0:            
    if x % 4 ==0 or x% 7 ==0 :
        print('YES')
    elif d == len(y):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
