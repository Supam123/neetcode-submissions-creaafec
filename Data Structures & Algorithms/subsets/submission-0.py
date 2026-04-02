class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        curr = []

        def backtrack(i):


            if(i== len(nums)):
                result.append(curr.copy()) # taking a copy and appending right away because 
                #curr gets modified oftenly so take a copy once we reach base case
                # finish it and boom its done
                return

            

            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            
            backtrack(i+1)
        backtrack(0)
        return result
        