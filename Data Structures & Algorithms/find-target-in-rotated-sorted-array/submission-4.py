class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while  l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[-1] : #means im in lowerhalf
                if target <= nums[-1]  and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # means im in higher half
                if target >= nums[0] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

               
        


        