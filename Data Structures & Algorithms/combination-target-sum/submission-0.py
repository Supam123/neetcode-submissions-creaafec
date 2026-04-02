class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        resultSum = 0
        resultList = []
        currList = []
        def backtrack(i,resultSum):
            if(resultSum == target):
                resultList.append(currList.copy())
                return
            
            if(i>=len(nums) or resultSum>target):
                return
            
            resultSum+=nums[i]
            currList.append(nums[i])
            backtrack(i,resultSum)

            currList.pop()
            resultSum-=nums[i]
            backtrack(i+1,resultSum)
      
        backtrack(0,0)
        return resultList

        