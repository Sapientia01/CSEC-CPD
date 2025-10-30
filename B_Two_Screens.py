t = int(input())
for _ in range(t):
    word1 = input()
    word2 = input()
    i = 0
    j = 0
    steps = 0
    while word1[i] == word2[j] and i < len(word1)-1 and j < len(word2)-1:
        i+=1
        j+=1
    if word1[i] == word2[j]:
        i+=1
        j+=1
        
    if i > 0:
     steps += i + 1
    steps += (len(word1)-i)
    steps += (len(word2)-j)

    print(steps)
