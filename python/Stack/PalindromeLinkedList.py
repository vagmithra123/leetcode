'''
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 


'''

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        mystack = []
        temp = head
        
        while temp:
            mystack.append(temp.val)
            temp = temp.next
            
        while head:
            if head.val != mystack[-1]:
                return False
            else:
                mystack.pop()
                head = head.next
                
        return True
            