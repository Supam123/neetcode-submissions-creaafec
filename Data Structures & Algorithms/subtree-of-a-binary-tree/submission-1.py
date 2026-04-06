# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(p,q):
            if p is None and q is None:
                return True
            if p and q and p.val== q.val :
                return ( isSame(p.left,q.left) and isSame(p.right,q.right))
            else:
                return False
        def dfs(root):
            if root is None:
                return False       
            if isSame(root,subRoot):
                return True
            else:
                                                             
                    return (dfs(root.left) or   dfs(root.right) )
        return dfs(root)
            










        