class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res  = []
        subset = []
        def dfs(i,curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            if curr_sum>target:
                return
            if i == len(nums):
                return

            subset.append(nums[i])
            dfs(i,curr_sum+nums[i])

            subset.pop()
            dfs(i+1,curr_sum)
        dfs(0,0)
        return res

    
        