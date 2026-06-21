class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for nodes in range(1,n+1):
            adj[nodes] = []
        for u,v,t in times:
            adj[u].append((t,v))
        shortest = {}
        h = []
        h.append((0,k)) # the minimum time to reach node k is 0
        while h:
            t1,n1 = heapq.heappop(h)
            if n1 in shortest: # if i have already calcualted the shortest path skip
                continue
            shortest[n1] = t1
            for t2,n2 in adj[n1]: # for all the immediate neigboirs of this node
                if n2 not in shortest:
                    heapq.heappush(h,(t1+t2,n2))
        if len(shortest) != n:
            return -1
        return max(shortest.values())
