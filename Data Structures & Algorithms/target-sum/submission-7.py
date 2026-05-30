class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i,capacity):
            if i == len(nums) and capacity == target:
                return 1
            if i == len(nums) and capacity != target:
                return 0
            if (i,capacity) in memo:
                return memo[(i,capacity)]
            
            add =  dp(i+1,capacity+nums[i])
            diff =  dp(i+1,capacity-nums[i])
            memo[(i,capacity)] =  add + diff
            return memo[(i,capacity)]
        return dp(0,0)
        