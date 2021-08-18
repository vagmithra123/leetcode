'''
152. Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        B = nums[::-1]
        
        for i in range(1, len(nums)):
            if nums[i-1] != 0:
                nums[i] *= nums[i-1]
                
        for i in range(1, len(B)):
            if B[i-1] != 0:
                B[i] *= B[i-1]
                
        return max(nums + B)
       

