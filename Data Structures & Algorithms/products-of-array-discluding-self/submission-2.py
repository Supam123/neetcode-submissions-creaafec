class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        l,r = 1,1
        '''
       1[1,2,4,6]
        [1,24,12,8]
        '''
        for i in range(0,len(nums)):
            if i != 0:
                l = l * nums[i-1]
            arr.append(l)
        for j in range(len(nums)-2,-1,-1):
            r = r * nums[j+1]
            arr[j] = arr[j] * r
        return arr


        