t = int(input())

for _ in range(t):

    n, c = input().split()
    n = int(n)

    colors = input()

    colors = colors+colors
    left, right = 0, 0
    max_val = 0
    coutn = 0
    state = False

    if c == "g":
        
        print(0)
        continue
        

    while left <= n:

        if colors[left] == c and colors[right] == "g":

            time = right - left

            if time > max_val:
                max_val = time
            left = right
            right += 1
            
        elif colors[left] == c and colors[right] != "g":
            right += 1

        elif  colors[left] != c:
            left +=1

        else:
            right+=1

    print(max_val)