'''
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false

'''

def isSymmetricBt(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            else:
                return node1.val == node2.val and isSymmetricBt(node1.left, node2.right) and isSymmetricBt(node1.right, node2.left)
            
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return isSymmetricBt(root.left, root.right)
    
    
        