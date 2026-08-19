class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        k = len(s1)
        h1 = {}
        h2 = {}
        for i in range(len(s1)):
            if s1[i] not in h1:
                h1[s1[i]] =1  
            else:
                h1[s1[i]] += 1

        while  r < len(s2):
            if s2[r] not in h2:
                h2[s2[r]] = 1
            else:
                h2[s2[r]] += 1
            if (r-l+1) == k:
                if h1 == h2:
                    return True
                else:
                    h2[s2[l]] -= 1
                    if h2[s2[l]] == 0:
                        del[h2[s2[l]]]
                    l += 1
            r += 1
        return False 