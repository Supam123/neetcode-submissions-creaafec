import sys
sys.setrecursionlimit(3000)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dp(curr,prev):
            if curr == len(nums):
                return 0 # because value at index n cannot be added so its zero 
            
            if (curr,prev) in memo:
                return memo[(curr,prev)]
            take = 0
            if prev == -1 or nums[curr] > nums[prev]:
                # i only take the current elemne tif its greater than ym prev
                take = 1 +  dp(curr+1,curr)   # we take the number hence the plsu 1
            # then i move to next index which becaisme cur for next one and prev is the 
            #one that i just took i
            skip  = dp(curr+1,prev)  # over here my i stays the old prev
            memo[(curr,prev)] = max(take,skip) # which ever gives me the longest streak

            return memo[(curr,prev)]
        return dp(0,-1)


        