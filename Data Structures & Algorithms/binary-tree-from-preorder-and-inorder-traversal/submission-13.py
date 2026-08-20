# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = 0
        inorder_map = {val:index for index,val in enumerate(inorder)}

        def dfs(l,r):
            nonlocal index
            if l > r :
                return None
            
            root = preorder[index]
            root =  TreeNode(root,None,None)
            index += 1
            mid = inorder_map[root.val]
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root
        return dfs(0,len(inorder)-1)










        