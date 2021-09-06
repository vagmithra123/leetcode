'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        count = 0
        for r in range(len(s)):
            if s[r] not in seen:
                count = max(count, r-l+1)
                
            else:
                if seen[s[r]] < l:
                    count = max(count, r-l+1)
                else:
                    l = seen[s[r]] + 1
                    
            seen[s[r]] = r
        
        return count
        