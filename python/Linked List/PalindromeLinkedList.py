'''

Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        myStack = []
        temp = head
        
        while temp is not None:
            myStack.append(temp.val)
            temp = temp.next
            
       
        
        while head is not None:
            if myStack[-1] != head.val:
                return False
            else:
                myStack.pop()
                head = head.next
                
        return True
        