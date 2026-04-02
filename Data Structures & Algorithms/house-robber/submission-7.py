class Solution:
    def rob(self, nums: List[int]) -> int:
        # cache = {}
        # def dfs(i):
        #     if(i>=len(nums)):
        #         return 0
        #     if(i in cache):
        #         return cache[i]
        #     cache[i] =  max(nums[i]+dfs(i+2),dfs(i+1))
        #     return cache[i]
        # return dfs(0)
    
        rob1,rob2 = 0,0
        for i in nums:
            mx= max(i+rob1,rob2)
            rob1 = rob2
            rob2 = mx
        return rob2
        
        





