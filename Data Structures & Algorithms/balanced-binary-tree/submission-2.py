# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return [True, 0]
            
            lheight = height(node.left)
            rheight = height(node.right)

            balanced = abs(lheight[1] - rheight[1]) <= 1 and lheight[0] and rheight[0]

            return [balanced, max(lheight[1], rheight[1]) + 1]
        
        return height(root)[0]
        
        