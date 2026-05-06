class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjL = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adjL[n1].append(n2)
            adjL[n2].append(n1)
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in adjL[node]:
                if nei in visited:
                    continue
                dfs(nei)
        islands = 0
        for k in range(n):
            if k not in visited:
                dfs(k)
                islands += 1
        return islands


        