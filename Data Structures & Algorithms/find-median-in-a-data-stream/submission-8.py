class MedianFinder:

    def __init__(self):
      self.small = [] #max heap
      self.large = [] #min heap
      heapq.heapify(self.small)
      heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
      heapq.heappush(self.small,-num)
      
      if self.small and self.large and -1*self.small[0] > self.large[0]:
        #perform swap
        val = heapq.heappop(self.small)
        heapq.heappush(self.large,-1*val)

      if abs(len(self.small) - len(self.large)) > 1:
        if len(self.small) > len(self.large):
           #perform swap
          val = heapq.heappop(self.small)
          heapq.heappush(self.large,-1*val)
        else:
          val = heapq.heappop(self.large)
          heapq.heappush(self.small,-1*val)

    def findMedian(self) -> float:
      if len(self.small) > len(self.large):
        return -1*self.small[0]
      if len(self.large) > len(self.small):
         return self.large[0]
      return (-1*self.small[0]+self.large[0])/2














    
        
        