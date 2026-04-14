class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for i in range(len(points)):
            distance =  math.sqrt(points[i][0] **2 + points[i][1]**2)
            heapq.heappush(h,(distance,points[i])) #min heap
        
        res = []
        i = 0
        while i != k:
            val = heapq.heappop(h)
            res.append(val[1])
            i+=1
        return res
        