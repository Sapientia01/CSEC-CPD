t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    word1 = sorted(list(input()))
    word2 = sorted(list(input()))
    word3 = ''
    i = 0
    j = 0
    a = 0
    b = 0

    while i < n and j < m:
        if word1[i] <  word2[j] and a < k:
            word3 += word1[i]
            i += 1
            a += 1
            b  = 0    
        elif i < n and word1[i] >  word2[j] and b < k :
           word3 += word2[j]
           j+=1 
           b += 1
           a = 0 
                     
        if a == k and j < m and i < n:
            word3 += word2[j]
            j +=1
            b +=1
            a = 0
        elif b == k and i < n and j < m:
            word3 += word1[i]
            i +=1
            a +=1
            b = 0
    print(word3)