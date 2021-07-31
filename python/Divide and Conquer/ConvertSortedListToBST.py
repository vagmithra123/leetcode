# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        Arr, n = [], head
        while n:
            Arr.append(n.val)
            n = n.next
        def make(low,high):
            if low<=high:
                mid       =  (low+high)//2
                root       = TreeNode(Arr[mid])
                root.left  = make(low  ,mid-1)
                root.right = make(mid+1,high  )
                return root
        return make(0, len(Arr)-1)
