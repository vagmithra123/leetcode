'''
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

def checkBST(root: TreeNode, lower: int, upper: int) ->bool:
    if root is None:
        return True
    if root.val  < lower or root.val > upper:
        return False
    return checkBST(root.left, lower, root.val-1) and checkBST(root.right, root.val+1, upper)

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return checkBST(root, -float('inf'), float('inf'))
   