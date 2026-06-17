class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # res = [0,0,0]
        # for t in triplets:

        #     if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
        #         # its a safe triplet
        #         res = [ max(res[0],t[0]),max(res[1],t[1]),max(res[2],t[2]) ]
        # return res == target
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue # we discard it 
            
            for i,v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3


