t = int(input())
for _ in range (t):
    s1 = input()
    s2 = input()

    n = len(s1)
    m = len(s2)

    res = 0

    i = 0
    j = 0
    while i < n and j < m and s1[i] == s2[j]:
        i += 1
        j += 1
        res += 1

    if  res > 0:
        res += 1

    res += (n-i) + (m-j)    

    print(res)

    


    