class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # here order does not matter
        # [1,2] is same as [2,1] order does not matter 
        # pick and skip
        
        '''
        my subset will keep on appendin g elements and eventually i will hit base case so we
        append it to res and trhen now subest is already 1,2,3 so we need to calculate other
        paths with other decision trees. we say hmm actually let me clear it out subset
        '''
        
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums): 
                return res.append(subset.copy())
            
            subset.append(nums[i]) #we take nums[i]
            dfs(i+1)

            subset.pop() # we can pop nums[i]
            dfs(i+1)
        dfs(0)
        return res

        