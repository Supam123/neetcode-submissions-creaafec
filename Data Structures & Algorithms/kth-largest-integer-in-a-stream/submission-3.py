class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.myHeap = nums # name our list
        self.k = k 
        heapq.heapify(self.myHeap) #O(n) min-heap make our heap
        # lets say nums are 1,2,3,4,5,6,7,8,9 and k = 3 
        # our heap will be  9,8,7,6,5,4,3,2,1 and k = 3
        # we keep popping smallest numbers untill heap is size k
        # heap after pops will be 9,8,7 kth largets is 7
        while len(self.myHeap) > k:
            heapq.heappop(self.myHeap)

    def add(self, val: int) -> int:

        heapq.heappush(self.myHeap,val)
        # leetcode keeps calling add and ading vals to my heap
        if len(self.myHeap) > self.k: # if the length is greate than k then we remove the smallerst elements
            heapq.heappop(self.myHeap)
        
        return self.myHeap[0]
        
