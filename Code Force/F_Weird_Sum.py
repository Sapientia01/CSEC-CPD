# n,m = map(int,input().split())
# matrix = []
# leng = 0
# for i in range(n):
#      l = list(map(int,input().split()))
#      matrix.append(l)
# for j in range(n):
#     for i in range(m):
#         color = matrix[j][i]
#         matrix[j][i] = ' '
#         for y in range(n):
#             for x in range(m):
#                 if matrix[y][x] == color :
#                     leng += ((abs(y-j) + abs(x-i)))

# print(leng)



# n,m = map(int,input().split())
# matrix = []
# l_m = []
# leng = 0
# for i in range(n):
#      l = list(map(int,input().split()))
#      l_m.extend(l)
# x = max(l_m)
# for i in range(n*m):
#      color = l_m[i]
#      l_m[i] = ' '
#      for j in range(n*m):
#           if l_m[j] == color:
#                c_r = i//m
#                c_c = i %m
#                e_r = j//m
#                e_c = j %m
#                leng += ((abs(c_r - e_r) + abs(c_c - e_c)))
# print(leng)








# n,m = map(int,input().split())
# matrix = []
# l_m = []
# leng = 0
# for i in range(n):
#      l = list(map(int,input().split()))
#      l_m.extend(l)
# x = max(l_m)
# colors_i = [[]]* (x+1)
# # print(colors_i)

# for i in range(n*m):
#      color = l_m[i]
#     #  print(color)
#      colors_i[color].append()

#     #  


# print(colors_i)
# # print(leng)




n,m = map(int,input().split())
matrix = []
leng = 0
for i in range(n):
     l = list(map(int,input().split()))
     matrix.append(l)
# print(matrix)
colors_i = list([[]]* (n*m) )



for j in range(n):
    for i in range(m):
        color = matrix[j][i]
    colors_i[color].append(j)
        # print(color)
        
print(colors_i)
# print(leng)
