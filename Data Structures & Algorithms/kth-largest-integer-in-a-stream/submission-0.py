class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k : # this makes sure that we have only k items 
          heapq.heappop(self.minHeap)
        # we assign min heap to list we hepaify the list
        #that ocnverts the list into heap 
        #we then only care about the k items in the heapr
        #because if we can maintain a heap with k items that would mean the root 
        # would be the smallest(min heap) out of all the k items 
        
    
        
        

    def add(self, val: int) -> int:

        heapq.heappush(self.minHeap, val)
 #automatically inserts new value into heap and puts it 
        #at the right place it might be larger than the k items then we just pop it
        #or it moght be smaller than the k items so it percolates up and gets inserted at right spot

        if(len(self.minHeap) > self.k):
             heapq.heappop(self.minHeap)
        return self.minHeap[0]

