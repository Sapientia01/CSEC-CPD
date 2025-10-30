t = int(input())
for _ in range(t):
    n = int(input())
    passagers = list(map(int, input().split()))

    left_chair = passagers[0]-1
    right_chair = passagers[0]+1
    answer = 'YES'
    for i in passagers[1:]:
        if i == left_chair:
            left_chair -= 1
        elif i == right_chair:
            right_chair +=1
        else:
            answer = 'NO'
            break
    print(answer)
