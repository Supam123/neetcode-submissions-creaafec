class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.myHeap = nums
        self.k = k
        heapq.heapify(self.myHeap) #O(n) min-heap
        while len(self.myHeap) > k:
            heapq.heappop(self.myHeap)

    def add(self, val: int) -> int:

        heapq.heappush(self.myHeap,val)
        # leetcode keeps calling add and ading vals to my heap
        if len(self.myHeap) > self.k: # if the length is greate than k then we remove the smallerst elements
            heapq.heappop(self.myHeap)
        
        return self.myHeap[0]
        
