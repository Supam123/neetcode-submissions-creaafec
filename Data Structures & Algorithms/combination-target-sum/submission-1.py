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
            
          
            currList.append(nums[i])
            backtrack(i,resultSum +nums[i])

            currList.pop()
           
            backtrack(i+1,resultSum) # this will run when we pop the iterm from curr list and
            #we return back from the call to the pne before it
            # and it would have th sum without the nums[i] that we popped

      
        backtrack(0,0)
        return resultList

        