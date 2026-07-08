class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        XOR
        N ^ 0 = N
        N ^ N = 0  when they are duplcaites they all collapse to 0
        hence unique number ^ 0 = unique number
        '''
        res = 0
        for n in nums:
            res = res ^ n
        return res
       


        