class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums) 
        i, j = 0, len(nums)-1
        for index in reversed(range(len(nums))):
            left = nums[i]
            right = nums[j]
            
            if abs(left) > abs(right):
                res[index] = left**2
                i += 1
            else:
                res[index] = right**2
                j -=1
                
        return res