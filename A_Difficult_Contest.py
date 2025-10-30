t = int(input())
for _ in range(t):
    contest = input()

    i = 0

    while i < (len(contest)-2):
        if contest[i:i+3] == "NTT":
            contest = "TT" + contest[0:i+1] + contest[i+3:] 
        elif contest[i:i+3] == "FFT":
            contest = "T" + contest[0:i+2] + contest[i+3:] 

        i += 1


    print(contest)




# 
# 
# 
# 
# FFT  NTT