class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_map = {}
        for i in range(len(s)):
            idx_map[s[i]] = i
        
        l,r=0,0
        furthest=0
        res=[]
        while r<len(s):
            furthest = max(furthest,idx_map[s[r]])
            if r==furthest:
                res.append(r-l+1)
                l = r+1
            r+=1
        return res
