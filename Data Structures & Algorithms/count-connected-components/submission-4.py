class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjL = {i:[] for i in range(n)}
        for n1,n2 in edges:
            # since this is undirected if n1---n2 connect
            # n1 will have n2 as its neighbors  
            # n2 will have n1 as it neighbors 
            adjL[n1].append(n2) 
            adjL[n2].append(n1)
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in adjL[node]:
                if nei in visited:
                    continue
                dfs(nei)
        island = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                island+=1
        return island
