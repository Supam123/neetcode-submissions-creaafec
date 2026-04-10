# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        li = []
        def dfs(root):
            if root is None:
                return li.append('N')
            li.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(li)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            node = preorder[i]
            i += 1
            if node == 'N':
                return None
            
            node = TreeNode(int(node),None,None)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

        



        














