'''
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false

'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        
        word_dict = {}
        for a, b in zip(pattern , s.split()):
            if b in word_dict.values() and  a not in word_dict.keys():
                return False
            elif a in word_dict and word_dict[a] != b:
                return False
            else:
                word_dict[a] = b
                print(word_dict)
                
        return True
        