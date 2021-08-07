'''
Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


'''

# Solution1 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i],s[-i-1] = s[-i-1],s[i]
            
        



#Solution2 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i =0
        j = len(s)-1
        while(i <= j):
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        