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
        i, j = 1, len(height)-1
        ans = 0
        l_max, r_max = height[0], height[-1]
        while i <= j:
            if l_max < height[i]:
                l_max = height[i]
            if r_max < height[j]:
                r_max = height[j]
            if l_max < r_max:
                ans += l_max - height[i]
                i += 1
            else:
                ans += r_max - height[j]
                j -= 1
                
        return ans