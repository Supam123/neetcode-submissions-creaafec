class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i,j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if(i,j) in memo:
                return memo[(i,j)]
            res = False
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            #check for *
            if j+1 < len(p) and p[j+1] == '*':
                take = match and dp(i+1,j) # use the star 
                skip = dp(i,j+2) #we dont use the star
                res = take or skip
            
            elif match:
                res = dp(i+1,j+1)
            memo[(i,j)] = res
            return memo[(i,j)]
        return dp(0,0)
          
