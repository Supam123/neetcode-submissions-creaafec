class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        [1,2,0,1,0]
        [0,1,2,3,4]
furhtest 1,3 3 4 
        '''
        furthest = 0
        for i in range(len(nums)):
            
            if i > furthest: # illegal index cant even reach here , so cant even reach last index
                return False
            furthest = max(i+nums[i],furthest)
        return True