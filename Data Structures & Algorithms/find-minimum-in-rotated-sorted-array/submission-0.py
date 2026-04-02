class Solution:
    def findMin(self, nums: List[int]) -> int:
        # in a roatetd array there are two halfs
        # higher sorted half
        # lower sorted half
        # if our mid lands in higher sorted half we go right
        # if our mid lands in lower sorted half we record and go left greedy

        l = 0
        r =  len(nums) - 1
        ans = float("inf")
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= nums[-1]: # means we are in sorted half
                ans = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
        return ans
        