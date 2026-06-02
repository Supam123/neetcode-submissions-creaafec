class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {n:[] for n in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(node):

            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
         


        num_island = 0
        for i in range(n):
            if i not in visit:
                num_island += 1
                dfs(i)
        return num_island






























        adjL = {i:[] for i in range(n)}
        for node1,node2 in edges:
            adjL[node1].append(node2)
            adjL[node2].append(node1)
        visit = set()
        def dfs(node):

            visit.add(node)
            for nei in adjL[node]:
                if nei not in visit:
                    dfs(nei)
        island = 0
        for i in range(n):
            if i not in visit:
                island+=1
                dfs(i)
        return island

        