'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

'''

class Solution:
    def generate_res(self, open_count, closed_count, curr_string, res) -> List[str]:
        if open_count == 0 and closed_count == 0:
            res.add(curr_string)
            return
        
        if closed_count > open_count:
            self.generate_res(open_count, closed_count-1, curr_string + ")", res)
            
        if open_count > 0:
            self.generate_res(open_count-1, closed_count, curr_string + "(", res)
            
            
    def generateParenthesis(self, n : int) -> List[str]:
        res = set()
        self.generate_res(n, n, "", res)
        return list(res)
   