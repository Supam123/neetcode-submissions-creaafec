# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        same = True
        def dfs(p,q):
            nonlocal same
            if p is None and q is None:
                return None
            if (p is None and q is not None ) or (p is not None and q is None):
                same = False
            if same == False:
                return False
            
            if p.val == q.val:
                dfs(p.left,q.left)
                dfs(p.right,q.right)
            else:
                same = False
            return same
        dfs(p,q)
        return same










        