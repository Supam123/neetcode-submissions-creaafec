# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = float('-inf')

        def dfs(root):
            nonlocal total
            if root is None:
                return 0
            leftSum = dfs(root.left)
            rightSum = dfs(root.right)
            total = max( max(leftSum,0) + max(rightSum,0) + root.val, total)
            return root.val + max(max(leftSum,0),max(rightSum,0))
        dfs(root)
        return total