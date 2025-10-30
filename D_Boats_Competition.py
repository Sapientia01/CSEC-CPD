t = int(input())

for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    weights.sort()
    
    max_teams = 0

    for s in range(2, 2 * n + 1):
        left = 0
        right = n - 1
        teams = 0

        while left < right:
            if weights[left] + weights[right] == s :
                teams += 1
                left += 1
                right -= 1
            elif weights[left] + weights[right] < s:
                left += 1
            else:
                right -= 1
        
        max_teams = max(max_teams, teams)
    
    print(max_teams)
