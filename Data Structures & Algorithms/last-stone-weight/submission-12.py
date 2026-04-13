class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since we want the maximum we neagte the items
        h = [-n for n in stones]
        heapq.heapify(h) # 

        while len(h) > 1:
            x = heapq.heappop(h) # first max
            y = heapq.heappop(h) # second max
            if x != y:
                diff = x-y
                heapq.heappush(h,diff) # add that diff as -ve as well
        
        return -h[0] if len(h) == 1 else 0
        