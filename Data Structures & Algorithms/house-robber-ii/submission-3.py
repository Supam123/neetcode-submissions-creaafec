class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def linearRob(arr):
            memo = {}
            def dfs(i):
                if i == 0:
                    return arr[0]
                if i == 1:
                    return max(arr[0],arr[1])
                if i in memo:
                    return memo[i]
                memo[i] = max(arr[i]+dfs(i-2),dfs(i-1))
                return memo[i]
            return dfs(len(arr)-1)
        return max(linearRob(nums[:-1]) , linearRob(nums[1:]))
        
            
         
        