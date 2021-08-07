'''
41. First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

'''



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
            
       
        