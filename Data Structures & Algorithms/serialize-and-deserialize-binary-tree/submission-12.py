# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            nonlocal res
            if root is None:
                res.append('N')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)

        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            root = data[i]
            i += 1
            if root  == 'N':
                return None
            root = TreeNode(int(root))
            root.left = dfs()
            root.right =  dfs()
            return root
        return dfs()
            







