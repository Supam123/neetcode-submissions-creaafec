
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
        # memo = {}
        # def dp(i):
        #     if i in memo:
        #         return memo[i]
        #     best = 1
        #     for j in range(i+1,len(nums)):
        #         if nums[j] > nums[i]:
        #             best = max(best,1 + dp(j))
        #     memo[i] = best
        #     return memo[i]
        
        # return max(dp(i) for i in range(len(nums)))
        #look at cvlaude nots

       



        # memo = {}
        # def dp(curr,prev):
        #     if curr == len(nums):
        #         return 0 # because value at index n cannot be added so its zero 
            
        #     if (curr,prev) in memo:
        #         return memo[(curr,prev)]
        #     take = 0
        #     if prev == -1 or nums[curr] > nums[prev]:
        #         # i only take the current elemne tif its greater than ym prev
        #         take = 1 +  dp(curr+1,curr)   # we take the number hence the plsu 1
        #     # then i move to next index which becaisme cur for next one and prev is the 
        #     #one that i just took i
        #     skip  = dp(curr+1,prev)  # over here my i stays the old prev
        #     memo[(curr,prev)] = max(take,skip) # which ever gives me the longest streak

        #     return memo[(curr,prev)]
        # return dp(0,-1)


        