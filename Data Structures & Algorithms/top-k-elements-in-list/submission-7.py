class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        buckets = [[]   for _ in range(0,len(nums)+1)]
        for key,value in hashmap.items():
            buckets[value].append(key)
        
        # now i have to return the k most elements
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
   
                



        