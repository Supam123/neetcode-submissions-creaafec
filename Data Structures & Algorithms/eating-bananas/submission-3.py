import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursTaken(mid):
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            return hours <= h
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l+r)//2

            if hoursTaken(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid +  1
        
        return ans