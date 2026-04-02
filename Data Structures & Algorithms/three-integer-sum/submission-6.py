class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            anchor = i
            l = anchor + 1
            r = len(nums) -1
            while l < r :
                total = nums[anchor] + nums[l] + nums[r]
                triplet = []
                if total >0 :
                    r -=1
                elif total < 0:
                    l += 1
                else:
                    triplet.append(nums[anchor])
                    triplet.append(nums[l])
                    triplet.append(nums[r])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    r-=1
                    res.append(triplet)
        return res
        



        