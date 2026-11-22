# Definition for a binary tree node.
# class TreeNode:
#     def __init__(root, val=0, left=None, right=None):
#         root.val = val
#         root.left = left
#         root.right = right

import math 

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        res = arr[1] - arr[0]
        for i in range(2, len(arr)):
            res = min(res, arr[i] - arr[i-1])
        return res