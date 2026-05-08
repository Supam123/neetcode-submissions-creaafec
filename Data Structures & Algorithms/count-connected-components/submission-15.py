class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        island = 0
        adjL = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adjL[n1].append(n2)
            adjL[n2].append(n1)
        visit = set()
        def dfs(node):
            for nei in adjL[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
        
        for i in range(n):
            if i not in visit:
                island+=1
                dfs(i)
        return island
                
        