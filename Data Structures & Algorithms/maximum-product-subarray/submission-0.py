class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = nums[0]
        curr_max , curr_min =1,1
        for n in nums:
            new_max = max(n,curr_min*n, curr_max*n)
            new_min = min(n,curr_min*n,curr_max*n)
            result =max(new_max,result)
            curr_max,curr_min=new_max,new_min
        return result
