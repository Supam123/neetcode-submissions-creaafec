class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = []
        #O(n)
        for i in range(len(points)):
            x,y = points[i][0],points[i][1]
            distance = x**2 + y**2
            h.append((distance,[x,y]))
        
        #convert h to min heap takes O(n)
        heapq.heapify(h)

        res = []
        # k times log n operations
        i = 0
        while i != k:
            val = heapq.heappop(h)
            res.append(val[1])
            i += 1
        return res