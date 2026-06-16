class Solution:
    def canJump(self, nums: List[int]) -> bool:

        furthest = 0
        for i in range(len(nums)):
            
            if i > furthest: # illegal index cant even reach here , so cant even reach last index
                return False
            furthest = max(i+nums[i],furthest)
        return True