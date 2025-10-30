class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_sum = sum(nums)
        max_scores = []
        left_score = 0
        right_score = nums_sum 
        max_score = left_score + right_score
        i = 0
        for x in nums:
            total_score = left_score + right_score 
            if x == 0 :
                left_score +=1
            else:
                right_score -= 1  
            if total_score > max_score:
                max_score = total_score
                max_scores = [i]
            elif total_score == max_score:
                max_scores.append(i)
            i += 1
        if n-nums_sum > max_score:
            max_scores = [i]
        elif n-nums_sum == max_score:
            max_scores.append(i)
        return max_scores
