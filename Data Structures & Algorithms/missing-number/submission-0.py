class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        res = 3
        i 0,1,2
        now we may wonder what bout i = 3 we donr hvae that 
        well we have res  = len nums = 3
        nums =1,2,3 
        i = 0 ,1, 2, and 3 from res 
        wehn  xored togther duplciate fade loner stayes which ismissing vlaue
        '''
        res =  len(nums)    
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res
