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
        i = len(buckets)-1
        count = 0
        output = []
        while i > 0:
            if( len(buckets[i])>= 1):
                for j in buckets[i]:
                    if(len(output) < k):
                        output.append(j)
            i -=1
        return output
                



        