class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if(nums[i] != val): 
                nums[k] = nums[i]
                k+=1
        return k

            # we will send i out to go to the number that not
            # equal to val and place it in the front of the array at k
        