'''

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false


'''

import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set(string.ascii_lowercase)
        
        if set(sentence) >= set(alphabet):
            return True
        else:
            return False