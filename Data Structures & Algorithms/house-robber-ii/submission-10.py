class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def linearRob(arr):
            # memo = {}
            # def dfs(i):
            #     if i == 0:
            #         return arr[0]
            #     if i == 1:
            #         return max(arr[0],arr[1])
            #     if i in memo:
            #         return memo[i]
            #     memo[i] = max(arr[i]+dfs(i-2),dfs(i-1))
            #     return memo[i]
            # return dfs(len(arr)-1)
            if len(arr) == 1:
                return arr[0]
            twoStepBack = arr[0]
            oneStepBack = max(arr[0],arr[1])
            for i in range(2,len(arr)):
                curr = max(arr[i]+twoStepBack,oneStepBack)
                twoStepBack = oneStepBack
                oneStepBack = curr
            return oneStepBack
        return max(linearRob(nums[:-1]) , linearRob(nums[1:]))
        
            
         
        