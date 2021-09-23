'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        trappedWater = 0
        maxLeft , maxRight = height[0], height[-1]
        i, j = 1, len(height)-2
        while i <= j:
            if maxLeft < height[i]:
                maxLeft = height[i]
            if maxRight < height[j]:
                maxRight = height[j]
            if maxLeft < maxRight:
                trappedWater += maxLeft - height[i]
                i += 1
            else:
                trappedWater += maxRight - height[j]
                j -= 1
        return trappedWater
        