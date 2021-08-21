'''
1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

'''

class Solution:
    def subdict(self, d1:Dict[str, int], d2:Dict[str, int])  -> bool:
        for k, count in d1.items():
            if k not in d2 or count > d2[k]:
                return False
        return True
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsDict = Counter(chars)
        total = 0
        for word in words:
            wd = Counter(word)
            if self.subdict(wd, charsDict):
                total += len(word)
        return total
                
      
        
        