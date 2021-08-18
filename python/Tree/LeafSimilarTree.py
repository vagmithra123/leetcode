'''

872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:

Input: root1 = [1], root2 = [1]
Output: true
Example 3:

Input: root1 = [1], root2 = [2]
Output: false
Example 4:

Input: root1 = [1,2], root2 = [2,2]
Output: true
Example 5:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_list1 = []
        leaf_list2 = []
        def getLeafNodes(root, leaf_list):
            if root is None:
                return
            if root.left is None and root.right is None:
                leaf_list.append(root.val)
                
            if root.left is not None:
                getLeafNodes(root.left, leaf_list)
                
            if root.right is not None:
                getLeafNodes(root.right, leaf_list)
                
            return leaf_list
        
        list1 = getLeafNodes(root1, leaf_list1)
        list2 = getLeafNodes(root2, leaf_list2)
        for a,b in zip_longest(list1, list2, fillvalue=0):
            if a != b:
                return False
            
        return True
        