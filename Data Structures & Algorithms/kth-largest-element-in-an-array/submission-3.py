class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)
        i = 0
        num = 0
        while i != k:
            num = heapq.heappop(h)
            i += 1
        return -num 

        