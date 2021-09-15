'''
917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        st = list(s)
        i, j = 0, len(st)-1
        while i < j:
            if not st[i].isalpha():
                i += 1
            if not st[j].isalpha():
                j -= 1
            if st[i].isalpha() and st[j].isalpha():
                st[i], st[j] = st[j], st[i]
                i += 1
                j -= 1
                
        return ''.join(st)
                
                