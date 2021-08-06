'''

704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums : return -1
        def recSearch(nums,target,left,right):
            if left>right : return -1
            mid = (left+right)//2
            if target == nums[mid] : return mid
            elif target<nums[mid]: return recSearch(nums,target,left,mid-1)
            else: return recSearch(nums,target,mid+1,right)
        return recSearch(nums,target,0,len(nums)-1)
        
        
        