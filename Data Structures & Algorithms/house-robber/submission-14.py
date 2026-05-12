class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = {}
        # def dp(i):
        #     if i == 0:
        #         return nums[0] # max i can do is robbing this house
        #     if i == 1:
        #         return max(nums[0],nums[1]) # max of house 0 or 1
        #     if i in memo:
        #         return memo[i] # if alreayd sovled return memo i
        #     memo[i] = max(nums[i]+dp(i-2), dp(i-1))
        #     return memo[i]
        # return dp(len(nums)-1)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
  
        twoStepBack = nums[0]
        oneStepBack = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            curr = max(nums[i]+twoStepBack, oneStepBack)
            twoStepBack =  oneStepBack
            oneStepBack = curr
        return oneStepBack
