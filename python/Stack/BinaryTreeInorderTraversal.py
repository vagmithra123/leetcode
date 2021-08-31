'''

94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def inorderTraversalHelper(root):
            if not root:
                return
            inorderTraversalHelper(root.left)
            output.append(root.val)
            inorderTraversalHelper(root.right)
            
        inorderTraversalHelper(root)
        return output
            
        
        
        