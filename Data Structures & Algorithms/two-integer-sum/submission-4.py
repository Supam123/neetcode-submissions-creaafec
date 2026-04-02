class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
    
        for i in range(len(nums)):
            res = target - nums[i]
            if res not in seen:
                seen[nums[i]] = i
            else:
                
                return [seen[res],i]

 
                

        
        