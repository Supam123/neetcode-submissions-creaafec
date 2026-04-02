from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        res = []
        deq = deque()
        while r < len(nums):
            

            # add that to my deque so the max stays in front always
            if not deq: # first time when deq is empty
                deq.append(r)
            else:
                while deq and nums[r] > nums[deq[-1]]: 
                # check if the new item is bigger than the 
                # previous one if it is then remove the smaller ones and place this one 
                # since for the current window there exist a vlaue greater than the left ones
                    deq.pop()
                deq.append(r)
        
            if r-l+1 == k:
                res.append(nums[deq[0]]) # we get the max 
                
                if deq[0] == l: 
                # we move l +1 so we check if the front 
                #of the deque is also l if it is we dont wanna leave the ghost behind 
                #so we remove it 
                    deq.popleft()
                l+=1
            r+=1
        return res






        