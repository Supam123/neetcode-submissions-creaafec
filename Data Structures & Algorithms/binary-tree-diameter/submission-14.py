# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if root is None:
                return 0
            
            left_ht = dfs(root.left)
            right_ht = dfs(root.right)
            res = max(res,left_ht + right_ht)
            return 1 + max(left_ht,right_ht)

        dfs(root)
        return res


      















        
        