class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2 !=  0:
             return False
        memo = {}
        def dp(i,capacity):
            if capacity == 0:
                return True
            if capacity < 0 :
                return False
            if i >= len(nums):
                return False
            if (i,capacity) in memo:
                return memo[(i,capacity)]
            
            take = dp(i+1,capacity-nums[i])
            skip = dp(i+1,capacity)
            memo[(i,capacity)] = take or skip
            return  memo[(i,capacity)]
        return dp(0,target//2)
            
          