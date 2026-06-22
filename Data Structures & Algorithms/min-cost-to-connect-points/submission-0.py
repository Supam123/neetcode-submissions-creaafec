class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        dist = abs(x1 - x2) + abs(y1 - y2)
        points = [[0, 0], [2,  2], [3,3],[2,4],[4,2]] 
                  x1 x2    y1 y2 ...
        start anywhere node
        pick the nei with smallest cost/distance 
        add that node next 
        then visit that node and add all of its nei and if a nei is alrady cvisit dont visit again
        '''
        visit = set()
        cost = 0
        adj = defaultdict(list)
        N = len(points)
        for i in range(N):
            a,b =  points[i]
            for j in range(i+1,N):
                c,d = points[j]
                weight = abs(c - a) + abs(d - b)
                adj[(a,b)].append((weight,(c,d)))
                adj[(c,d)].append((weight,(a,b)))

        h = []
        heapq.heappush(h,(0,points[0][0],points[0][1])) # starting wt from self is 0
        while len(visit) < len(points):
            wt,x,y = heapq.heappop(h)
            if (x,y) in visit:
                continue # skip it 
            cost += wt
            visit.add((x,y))
            # go to its neig pick the one with minimum cost
            for nei in adj[(x,y)]:
                if (nei[1][0],nei[1][1]) not in visit:
                    heapq.heappush(h,(nei[0],nei[1][0],nei[1][1]))
        return cost


            




        