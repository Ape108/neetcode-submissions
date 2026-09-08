# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q) # should return LCA of left subtree
        right = self.lowestCommonAncestor(root.right, p, q) # should return LCA of right subtree

        if left and right:
            return root
        
        return left or right # returns left if non-null and right otherwise
        
