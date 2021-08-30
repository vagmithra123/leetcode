'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]


'''

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if (l1.val >= l2.val):
            ans = ListNode(l2.val)
            ans.next = self.mergeTwoLists(l1, l2.next)
        else:
            ans = ListNode(l1.val)
            ans.next = self.mergeTwoLists(l1.next, l2)
            
        return ans
        