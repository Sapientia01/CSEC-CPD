t = int(input())
for _ in range(t):
    n = int(input())
    seats  = [0 for i in range(n)]
    ord = list(map(int,input().split()))
    ans = "YES"
    seats[ord[0]-1] += 1

    for i in ord[1:]:
        i -= 1
        if i-1 >= 0 and seats[i-1] == 1 :
            seats[i] += 1

        elif  i < n-1  and  seats[i +1] == 1:
            seats[i] += 1

        else:
            ans = "NO"
            break

    print(ans)






# t = int(input())
# for _ in range(t):
#     n = int(input())
#     seats  = [0 for i in range(n)]
#     ord = list(map(int,input().split()))
#     ans = "YES"
#     seats[ord[0]-1] += 1
#     for i in ord[1:]:
#         if i-2 > 0 and seats[i-2] == 1 or i < n and seats[i] == 1:
#             seats[i-1] += 1
#         else:
#             ans = "NO"
#             break

#     print(ans)