# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        def dfs(root):
            if root is None:
                return s.append('N')
            s.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(s)
                
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder =  data.split(',')
        i = 0
        def dfs():
            nonlocal i
            if preorder[i] == 'N':
                i+= 1
                return None
            root = preorder[i]
            i += 1
            root = TreeNode(int(root),None,None)
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()














