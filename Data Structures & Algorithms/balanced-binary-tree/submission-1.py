# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def height(node):
            nonlocal isBalanced
            if not node:
                return -1
            
            lheight = height(node.left)
            rheight = height(node.right)

            if lheight - rheight > 1 or rheight - lheight > 1:
                isBalanced = False

            return max(lheight, rheight) + 1
        
        height(root)
        return isBalanced
        
        