class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "[{(":
                stack.append(i)
                continue
            if i in ")}]":
                if not stack:
                    return False
                elif i==")" and stack[-1]=="(":
                    stack.pop()
                elif i=="}" and stack[-1]=="{":
                    stack.pop()

                elif i=="]" and stack[-1]=="[":
                    stack.pop() 
                else: 
                    return False
        return not len(stack)
        
        