t = int(input())
for _ in range(t):
    n,k = list(map(int, input().split()))
    word = input()
    i = 0
    j = 0
    x = 0
    while j < len(word) and i < len(word):
        if word[i] == 'B':
            j += k
            x +=1
            i += k
        else:    
            i+=1

    print(x)    
