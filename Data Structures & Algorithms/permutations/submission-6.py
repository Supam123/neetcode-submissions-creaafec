class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        permutations order does not matter
        '''
        res = []
        path = []
        visit = set()
        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for j in nums:
                if j in visit:
                    continue

                visit.add(j)
                path.append(j)
                dfs()
                path.pop()
                visit.remove(j)
        dfs()
        return res
        