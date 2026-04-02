class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = 0
        # for i in range(len(nums)):
        #     if(nums[i] != val): 
        #         nums[k] = nums[i]
        #         k+=1
        # return k
        l = 0
        r = 0
        while r < len(nums):
         
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l 
    

            # we will send i out to go to the number that's not
            # equal to val and place it in the front of the array at k
        