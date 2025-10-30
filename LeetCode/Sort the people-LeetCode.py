"""" Sorting Using Insertion sorting """
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            for j in range(i+1,len(names)):
                if heights[j] >= heights[i]:
                    heights[j], heights[i] =  heights[i],  heights[j]
                    names[j], names[i] =  names[i],  names[j] 
        return names
"""" Sorting Using Counting sorting """
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        if len(heights) > 1:
            counting = [0]*(max(*heights)+1)    
            for i,height in enumerate(heights):
                counting[height] = names[i]
            j = 0    
            for i in range(len(counting)-1,0,-1):
                if counting[i] != 0:
                    names[j] = counting[i]
                    j += 1 
        return names
