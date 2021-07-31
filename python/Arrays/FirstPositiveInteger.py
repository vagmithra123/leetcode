class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #convert nums to set
        nums_set = set(nums)
        
        #Let's consider the smallest positive number 1
        smallest = 1
        
        while True:
            if smallest in nums_set:
                smallest +=1
                
            else:
                return smallest
            
       
        