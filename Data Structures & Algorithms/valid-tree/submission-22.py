class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        adjL = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adjL[n1].append(n2)
            adjL[n2].append(n1)
        def dfs(node,prevNode):

            visit.add(node)
            for nei in adjL[node]:
                if nei == prevNode:
                    continue
                if nei in visit:
                    return False
                if dfs(nei,node) == False:
                    return False
            return True
       
       
        return True if dfs(0,-1) == True and len(visit) == n else False
        