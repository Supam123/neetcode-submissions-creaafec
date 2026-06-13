class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        h = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(h, (intervals[i][1]-intervals[i][0]+1,intervals[i][1]))
                i += 1
            while h and h[0][1] < q:
                heapq.heappop(h)
            
            ans =  h[0][0] if h else -1
            res[q] = ans
        l = []
        for q in queries:
            l.append(res[q])
        return l

        