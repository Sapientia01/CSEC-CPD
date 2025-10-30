t = int(input())
for _ in range(t):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())

    len1 = len(str(x1)) + p1
    len2 = len(str(x2)) + p2

    if len1 > len2:
        print(">")
    elif len1 < len2:
        print("<")
    else:
        s1 = str(x1)
        s2 = str(x2)
        diff = len(s2) - len(s1)

        if diff > 0:
            s1 += "0" * diff
        elif diff < 0:
            s2 += "0" * (-diff)

        if s1 > s2:
            print(">")
        elif s1 < s2:
            print("<")
        else:
            print("=")












# t = int(input())
# for _ in range(t):
#     x1, p1 = map(int,input().split())
#     x2, p2 = map(int,input().split())

#     # num1 = x1 * (10**p1)
#     # num2 = x2 * (10**p2)
#     num1 = x1 * pow(10,p1)
#     num2 = x2 * pow(10,p2)

#     if num1 > num2:
#         print(">")

#     elif num1 < num2:
#         print("<")

#     else:
#         print("=")


