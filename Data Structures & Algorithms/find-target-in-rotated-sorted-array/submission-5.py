class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 # left boundary
        r = len(nums) - 1 # right boundary
        while  l <= r:
            mid = (l+r)//2 # calculate mid
            if nums[mid] == target: # mid lands = target
                return mid
            elif nums[mid] <= nums[-1] : #means im in lowerhalf
            # if i am in lower half and my target is also there then do BS there
                if target <= nums[-1]  and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # means im in higher half
         # if i am in higher half and my target is also there then do BS there
                if target >= nums[0] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

               
        


        