'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(0, len(nums)):
            dict[nums[i]] = dict.get(nums[i],0)+1
            
        return max(dict.items(), key = operator.itemgetter(1))[0]
        