class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        since we need unique order this is a pick skip flavor 1
        we can only choose one item at most once no resuse
        but since the given list can have duplicates and in order to prevent 
        duplicate combinations in the result such as [2,2,4] can be producded multiple times
        so we wanna branch it in a way that we dont have duplciates.
        '''
        nums = sorted(candidates)
        res = []
        subset = []
        def dfs(i,curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or curr_sum > target:
                return
            
            #include left branch nums[i] 
            subset.append(nums[i])
            dfs(i+1,curr_sum+nums[i])

            #skip nums[i] right branch and we skip all the duplicates
            # [1,2,2,4,5]
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1,curr_sum)
            

        dfs(0,0)
        return res