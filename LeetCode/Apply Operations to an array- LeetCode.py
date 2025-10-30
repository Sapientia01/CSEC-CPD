class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n-1:
            if nums[i] == nums[i+1] :
                nums[i] *= 2
                nums[i+1] = 0
                i += 2
            else:
                i += 1
        zeros = nums.count(0)
        for i in range(zeros):
            nums.remove(0)
        nums.extend([0]*zeros)            
        return nums 
