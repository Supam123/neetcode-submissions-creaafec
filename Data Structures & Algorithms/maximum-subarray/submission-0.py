class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        best = nums[0]
        for n in nums:
            if curr_sum <0: # since curr_sum is -ve its gonna bring down the sum
                curr_sum = 0
            curr_sum+=n
            best = max(best,curr_sum)
        return best
        