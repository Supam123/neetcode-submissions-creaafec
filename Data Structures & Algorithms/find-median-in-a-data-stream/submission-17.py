class MedianFinder:

    def __init__(self):
      self.h1 = []
      self.h2 = []
   
        

    def addNum(self, num: int) -> None:
      heapq.heappush(self.h1,-num)
      
      if self.h1 and self.h2 and -1*self.h1[0] > self.h2[0]:
        #perform swap
        val = heapq.heappop(self.h1)
        heapq.heappush(self.h2,-1*val)
      
      if abs(len(self.h1) - len(self.h2)) > 1:
        if len(self.h1) > len(self.h2):
          val = -1*heapq.heappop(self.h1)
          heapq.heappush(self.h2,val)
        else:
         
          val = heapq.heappop(self.h2)
          heapq.heappush(self.h1,-val)
        

    def findMedian(self) -> float:
      if len(self.h1) > len(self.h2):
        return -1* self.h1[0]
      elif len(self.h2) > len(self.h1):
        return self.h2[0]
      else:
       return (-1*self.h1[0]+self.h2[0])/2
        
        