class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue   
            a = i
            l = a + 1
            r = len(nums) - 1
            while l < r :
                total = nums[a] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[a],nums[l],nums[r]])
                    l += 1
                  
                    while l < r and  nums[l] == nums[l-1]:
                        l+=1
                    r -= 1
        return res




        
        
        
        

        