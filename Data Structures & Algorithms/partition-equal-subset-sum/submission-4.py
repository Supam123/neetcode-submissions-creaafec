class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        if sum(nums) %2 !=0:return False
        target  = sum(nums)/2
        #nums = 1,5,11,15
        for n in nums:
            newDp = set(dp)
            for val in dp:
                newDp.add(n+val) 
                '''
                now new dp contains all the older vlaues of old dp 
                and we add the n to all those values and then reasign it back
                to dp
                '''
            dp = newDp
            if target in dp:
                return True
        return False




        # total_sum = sum(nums)
        # memo ={}
        # def dp(i,capacity):
        #     if capacity == 0:
        #         return True
        #     if i == len(nums):
        #         return False
        #     if capacity <0:
        #         return False
        #     if (i,capacity) in memo:
        #         return memo[(i,capacity)]

        #     memo[(i,capacity)] = dp(i+1,capacity-nums[i]) or dp(i+1,capacity)
        #     return memo[(i,capacity)]
        # return dp(0,total_sum/2)
        