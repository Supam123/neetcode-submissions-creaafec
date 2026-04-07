# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root,maxi):
            nonlocal count
            if root is None:
                return None
            maxi = max(maxi,root.val)
            if root.val >= maxi:
                count += 1

            dfs(root.left,maxi)
            dfs(root.right,maxi)
        dfs(root,float('-inf'))
        return count
            
        