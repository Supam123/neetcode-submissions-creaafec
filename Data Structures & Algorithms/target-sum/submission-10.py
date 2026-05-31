class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # row_below = defaultdict(int)
        # row_below[target] = 1
        # for i in range(len(nums)-1,-1,-1):
        #     curr_row = defaultdict(int)
        #     for s,count in row_below.items():
        #         curr_row[s+nums[i]] = curr_row.get(s+nums[i],0) + count
        #         curr_row[s-nums[i]] = curr_row.get(s-nums[i],0) + count
        #     row_below = curr_row
        # return row_below[0]
        row_above = defaultdict(int)
        row_above = {0:1}
        for n in nums:
            curr_row =  defaultdict(int)
            for s,count in row_above.items():
                curr_row[s+n] =  curr_row.get(s+n,0) + count
                curr_row[s-n] =  curr_row.get(s-n,0) + count
            row_above = curr_row
        return row_above[target]

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
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
        