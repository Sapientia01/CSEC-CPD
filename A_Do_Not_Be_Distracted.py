from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    tasks = input()
    task_freq = Counter(tasks)
    l = 0
    r = 1
    answer = "YES"
    while l < n and r < n and n> 2:
        task = tasks[l] 
        if task !=  tasks[r]:
            if(task_freq[task] != (r-l)):
                answer ="NO"
                break
            else:
                 l = r
                 r+=1
        if r == n-1:
            break 
        elif task  ==  tasks[r]:
                r+=1
        if r == n-1:
            break        


    print(answer)
