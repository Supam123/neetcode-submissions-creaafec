class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def dp(leftWall,rightWall):
            if leftWall + 1 == rightWall:
                return 0
            if (leftWall,rightWall)  in memo:
                return memo[(leftWall,rightWall)]
            best = 0
            for k in range(leftWall+1,rightWall):
                coins = nums[leftWall] *nums[k]*nums[rightWall] + dp(leftWall,k) + dp(k,rightWall)
                best = max(best,coins)
            memo[(leftWall,rightWall)] = best
            return memo[(leftWall,rightWall)]
        return dp(0,len(nums)-1)
        