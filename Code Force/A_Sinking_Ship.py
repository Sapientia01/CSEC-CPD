n = int(input())

rats = []
w_and_c = []
man = []
cap = []

for _ in range(n):

    names = input().split()

    match names[-1]:

        case "rat":

            rats.append(names[0])

        case "woman" | "child":

            w_and_c.append(names[0])
        
        case "man":

                man.append(names[0])
            
        case "captain":

                cap.append(names[0])

for i in rats:
     print(i) 

for i in w_and_c:
     print(i) 

for i in man:
     print(i) 
                    
for i in cap:
     print(i)                