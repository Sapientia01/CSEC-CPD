t = int(input())
for _ in range(t):
    word= input()
    actual_word = []
    out = ''
    upper_pos = []
    lowwer_pos = []

    for i,letter in enumerate(word):

        if letter != "b" and letter != "B":
            actual_word.append(letter)
            if ord(letter) > 96:
                lowwer_pos.append(i) 
            else:
                upper_pos.append(i)
                


        elif letter == "b":
            actual_word.append(" ")
            if len(lowwer_pos) > 0:
                # print(actual_word,lowwer_pos)
                actual_word[lowwer_pos[-1]] =  " " 
                lowwer_pos.pop(-1)


        elif letter == "B":
            actual_word.append(" ")
            if len(upper_pos) > 0:
                actual_word[upper_pos[-1]] =  " "
                upper_pos.pop(-1)








    for i in actual_word:
        if i != " ":
            out += i

    print(out)










































# t = int(input())
# for _ in range(t):
#     word= input()
#     actual_word = ''
#     out = ''
#     upper_pos = []
#     lowwer_pos = []

#     for i,letter in enumerate(word):

#         if letter != "b" and letter != "B":
#             actual_word += letter
#             if ord(letter) > 96:
#                 lowwer_pos.append(i)
#             else:
#                 upper_pos.append(i)
                


#         elif letter == "b":
#             if len(lowwer_pos) > 0:
#                 actual_word = actual_word[0:lowwer_pos[-1]] + " " + actual_word[lowwer_pos[-1]+1:]
#                 lowwer_pos.pop(-1)


#         elif letter == "B":
#             if len(upper_pos) > 0:
#                 actual_word = actual_word[0:upper_pos[-1]] + " " +  actual_word[upper_pos[-1]+1:]
#                 upper_pos.pop(-1)

#     for i in actual_word:
#         if i != " ":
#             out += i

#     print(actual_word)









