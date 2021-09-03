'''
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

class Solution:
    def checkInclusion(self, target_string: str, string: str) -> bool:
        target_string = ''.join(sorted(target_string))
        curr_string = ""
        
        for char in string:
            curr_string += char
            
            if len(curr_string) == len(target_string):
                sorted_string = ''.join(sorted(curr_string))
                
                if sorted_string == target_string:
                    return True
                
                curr_string = curr_string[1:]
        return False
                
            
            
        