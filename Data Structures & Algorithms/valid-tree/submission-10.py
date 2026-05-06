class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjL = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adjL[n1].append(n2)
            adjL[n2].append(n1)
        visit = set()
        def dfs(node,prev_node):
            visit.add(node)
            for nei in adjL[node]:
                if prev_node  == nei:
                    continue
                if nei in visit:
                    return False
                if dfs(nei,node) == False:
                    return False
            return True
        if dfs(0,-1) == True and len(visit) == n:
            return True
        else:
            return False


                
               
        