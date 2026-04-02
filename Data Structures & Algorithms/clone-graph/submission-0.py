"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
for each neighbor, we'll first see if it already exists in the hashmap. 
If it does, no need to clone it again but we will 
add the value of that key from the hashmap to the current node's neighbors
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        old_to_new = {}

        def dfs(node):
            if (node in old_to_new):
                return old_to_new[node]
                
            cloned_node = Node(node.val)
            old_to_new[node] = cloned_node
            for nei in node.neighbors:
                cloned_node.neighbors.append(dfs(nei))
            return cloned_node
        return dfs(node) if node else None


        
        
        