# t= int(input())
# for j in range(t):
#     n = int(input())

#     word = list(input())
#     pairs = [" " for _ in range(n)]
#     out = [" " for _ in range(n)]
#     out[0] = word[0]
#     i = 0


#     for k,letter in enumerate(word):
#         if k < len(word)-1:
#             if letter == word[k+1]:
#                 pairs[k] = letter
#         if letter == pairs[k-1]:
#             pairs[k] = letter

#     print("".join(pairs))




    
#     for letter in word[1:]:
#         if i >= 0 and out[0] != " ":
#             if out[i] == letter:
#                 i += 1
#                 out[i] = letter
                

#             elif out[i] != letter:
#                 out[i] = " "
#                 i -= 1

#         elif i < 0 and out[0] == " ":
#             i += 1
#             out[i] = letter


#     max_len = 0
#     while out[max_len] != " ":
#         max_len+= 1

#     # print()
    



#     # print(j+1,max_len,"".join([i for i in out if  i != " "]))


















# # t= int(input())
# # for j in range(t):
# #     n = int(input())
    
# #     word = input()
# #     out = [" " for _ in range(n)]
# #     out[0] = word[0]
# #     i = 0

    
# #     for letter in word[1:]:
# #         if i >= 0 and out[0] != " ":
# #             if out[i] == letter:
# #                 i += 1
# #                 out[i] = letter
                

# #             elif out[i] != letter:
# #                 out[i] = " "
# #                 i -= 1

# #         elif i < 0 and out[0] == " ":
# #             i += 1
# #             out[i] = letter


# #     max_len = 0
# #     while out[max_len] != " ":
# #         max_len+= 1

# #     print()
    



# #     print(j+1,max_len,"".join([i for i in out if  i != " "]))

















import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        stack = []
        for char in s:
            if stack and stack[-1] != char:
                stack.pop()
            else:
                stack.append(char)
        output_lines.append(str(len(stack)))
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()