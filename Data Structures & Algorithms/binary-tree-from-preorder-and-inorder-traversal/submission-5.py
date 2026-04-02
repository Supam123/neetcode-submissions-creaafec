# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {val:index  for index,val in enumerate(inorder)}
        # value = its index in O(1) time complexity

        self.preorder_index = 0

        def dfs(in_left,in_right):
            if(in_left > in_right): # meaning we have reached base case leaf node
                return None 

            root_value = preorder[self.preorder_index]
            root = TreeNode(root_value)

            self.preorder_index +=1 # we move to the next node  and its always root node of that subtree

            root.left = dfs(in_left , inorder_map[root_value]-1) # -1 because that is my root node
            root.right = dfs(inorder_map[root_value]+1 , in_right)

            return root
        return dfs(0,len(inorder)-1)

        