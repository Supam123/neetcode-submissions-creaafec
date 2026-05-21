class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        valid tree is a tree with no cycle and all connected ocmponents
        '''
        visit = set()
        adj = {n :[] for n in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        def dfs(curr,prev):
            visit.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                if nei in visit:
                    return False
                if dfs(nei,curr) == False:
                    return False
               
            return True       
        if dfs(0,-1) == True and len(visit) == n:
            return True
        else:return False

        