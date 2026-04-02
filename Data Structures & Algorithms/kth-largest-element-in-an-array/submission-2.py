class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        count = 0
        while count !=k :
            x = heapq.heappop(heap)
            count+=1
        return -x

        