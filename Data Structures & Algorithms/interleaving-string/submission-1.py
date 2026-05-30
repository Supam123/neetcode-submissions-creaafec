class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        s1 = "aaaa", 
        s2 = "bbbb", 
        s3 = "aabbbbaa"
        '''
        if len(s3) != (len(s1) + len(s2)):
            return False
        memo = {}
        def dp(i,j):
            if i == len(s1) and j == len(s2):
                return True # we proceedes all chars in both strings hence true
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i < len(s1) and s3[i+j] == s1[i]:
                if dp(i+1,j): # if this path leads to true memo set to true return treu STOP we done
                    memo[(i,j)] = True
                    return True # stop we are done
            if j < len(s2) and s3[i+j] == s2[j]:
                if dp(i,j+1): # if this leads to a True path set memo to true return true we are done
                    memo[(i,j)] = True
                    return True
            # But if neither of the dp recursive calls are truer we never enter the if block
            # we never enter and return true so we set memo at that to false
            memo[(i,j)] = False
            return memo[(i,j)]
        return dp(0,0)
            
        