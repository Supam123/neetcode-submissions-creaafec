class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        n =  len(s)
        def dp(i):
            if i  == n:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = (dp(i+1) if int(s[i])!=0 else 0 ) + (dp(i+2) if i+1<n and 10<=int(s[i:i+2])<=26 else 0)
            return memo[i]
        return dp(0)
        