t = int(input())
for _ in range(t):
    m = int(input())
    temp = list(map(int,input().split()))
    n = int(input())
    for i in range(n):
        str = input()
        s_match = {}
        
        ans = "YES"
        if len(str) != m:
            ans = "NO"

        elif len(set(temp)) != len(set(str)):
            ans = "NO"
        else:
            for i in range(m):
                if str[i] in  s_match :
                    if  s_match [str[i]] != temp[i]:
                        ans = "NO"
                        break
                else:
                    s_match [str[i]] = temp[i]

        print(ans)