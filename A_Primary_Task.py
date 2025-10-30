t = int(input())
for _ in range(t):
    num = input()
    ans = "YES"
    if len(num) <= 2:
        ans = "NO"
    elif  num[:2] != "10":
        ans = "NO"
    elif  num[2] ==  "0":
        ans = "NO" 
    elif int(num[2:]) < 2 :
        ans = "NO" 

    print(ans)