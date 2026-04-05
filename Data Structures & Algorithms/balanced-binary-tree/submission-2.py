# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root):
            nonlocal balanced
            if root is None:
                return 0

            left_ht = dfs(root.left)
            right_ht = dfs(root.right)
            if abs(left_ht-right_ht) > 1:
                balanced =  False
            return 1 + max(left_ht,right_ht)
        dfs(root)
        return balanced

        