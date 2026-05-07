class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n =  len(edges) #usually edges are n-1 if n nodes but since his is a cycle so edges are = number of nodes.

        parent = {}
        rank = {}
        for i in range(1,n+1):
            parent[i] = i #each is its own parent
            rank[i] = 1 #each ahs ht = 1
        def find(node):
            res = node
            while res !=  parent[res]:
                parent[res] =  parent[parent[res]]
                res = parent[res]
            return res
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2 :
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1
            return True
        for node1,node2 in edges:
            if union(node1,node2) == False:
                return [node1,node2]
           











