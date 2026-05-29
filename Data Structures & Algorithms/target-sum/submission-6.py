class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        row_below = defaultdict(int)
        row_below[target] = 1
        for i in range(len(nums)-1,-1,-1):
            curr_row = defaultdict(int)
            for s,count in row_below.items():
                curr_row[s+nums[i]] = curr_row.get(s+nums[i],0) + count
                curr_row[s-nums[i]] = curr_row.get(s-nums[i],0) + count
            row_below = curr_row
        return row_below[0]
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # memo = {}
        # def dp(i,capacity):
        #     if i == len(nums) and capacity == target:
        #         return 1
        #     if i == len(nums) and capacity != target:
        #         return 0
        #     if (i,capacity) in memo:
        #         return memo[(i,capacity)]
            
        #     add = dp(i+1,nums[i]+capacity)
        #     subtract = dp(i+1,capacity-nums[i])
        #     memo[(i,capacity)] = add+ subtract
        #     return memo[(i,capacity)] 
        # return dp(0,0)
        