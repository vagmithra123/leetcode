'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

'''



class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        l = 0
        r = 0
        for i in range(0, len(s)):
            
            if s[i] == 'L':
                l += 1
            else:
                r += 1
            if l == r:
                count += 1
        return count
            
        