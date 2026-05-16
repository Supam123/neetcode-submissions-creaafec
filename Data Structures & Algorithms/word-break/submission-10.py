class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # memo = {}

        # def dp(i):
        #     if i  == len(s):
        #         return True
        #     if i in memo:
        #         return memo[i]
            
        #     for word in wordDict:
        #         if s[i:i+len(word)] == word:
                  
        #             if dp(i+len(word)) == True:
        #                 return True
        #             memo[i] =  False
        #     return False
        # return dp(0)

        n  = len(s)
        dp = [False]*(n+1)
        dp[-1] = True
        for i in range(n-1,-1,-1):
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]

        