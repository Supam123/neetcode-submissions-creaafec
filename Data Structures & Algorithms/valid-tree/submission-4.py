class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjL = {i:[] for i in range(n)}
        for n1,n2 in edges:
            # since this is undirected if n1---n2 connect
            # n1 will have n2 as its neighbors  
            # n2 will have n1 as it neighbors 
            adjL[n1].append(n2) 
            adjL[n2].append(n1)
        visited = set()
        def dfs(curr_node,previous_node):          
            visited.add(curr_node)
            for nei in adjL[curr_node]:
                if nei == previous_node:
                    continue
                if nei in visited:
                    return False
                if dfs(nei,curr_node) == False:
                    return False
       
            return True
        return True if dfs(0,-1) == True and len(visited) == n else False

        