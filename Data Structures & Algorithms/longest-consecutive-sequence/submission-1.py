class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #lookups will be constant
        longest = 0
        for n in nums:
            if(n-1 not in numSet):
                curr_num = n
                curr_streak = 1
                while (curr_num+1) in numSet :
                    curr_num +=1
                    curr_streak +=1
                
                longest = max(curr_streak,longest)
        return longest

            