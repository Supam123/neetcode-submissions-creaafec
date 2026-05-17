class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        memo ={}
        def dp(i,capacity):
            if capacity == 0:
                return True
            if i == len(nums):
                return False
            if capacity <0:
                return False
            if (i,capacity) in memo:
                return memo[(i,capacity)]

            memo[(i,capacity)] = dp(i+1,capacity-nums[i]) or dp(i+1,capacity)
            return memo[(i,capacity)]
        return dp(0,total_sum/2)
        