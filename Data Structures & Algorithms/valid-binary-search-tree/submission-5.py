# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root,min_val,max_val):
            
            if root is None:
                return True
            
            
            if  root.val < max_val and root.val > min_val:
                return (dfs(root.left,min_val,root.val) and dfs(root.right,root.val,max_val))
            else: return False
        return dfs(root,float('-inf'),float('+inf'))         
           
         
    
            
            
            
        