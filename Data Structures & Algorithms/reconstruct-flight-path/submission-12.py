class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        adj = defaultdict(list)
        for src,dst in tickets:
            adj[src].append(dst)
        
        result = []
        def dfs(node):

            while adj[node]:
                next_node = adj[node].pop()
                dfs(next_node)
            result.append(node)
        dfs('JFK')
        return result[::-1]

