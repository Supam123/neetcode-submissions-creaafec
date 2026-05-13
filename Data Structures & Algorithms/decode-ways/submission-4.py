class Solution:
    def numDecodings(self, s: str) -> int:
        # memo = {}
        # n =  len(s)
        # def dp(i):
        #     if i  == n:
        #         return 1
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = (dp(i+1) if int(s[i])!=0 else 0 ) + (dp(i+2) if i+1<n and 10<=int(s[i:i+2])<=26 else 0)
        #     return memo[i]
        # return dp(0)
        # '''
        # we start from 0 
        # and we return from 0 why becasue dp at 0 is the total number of ways to decore enditre string
        # then if i == n menaing we proccedes the entire string by making valid choices and there has to be atleast 1 eay so we return 1
        # then memo i to avoid recomputation
        # and then if i choose i char then i go i +1 and if i choose s[i:i+2] chars  menaingf i and i +1 then i call i+2 only if htey are vlaid
        # '''
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1,-1,-1):
            one = 0
            two = 0
            if s[i]!='0':
                one = dp[i+1]
            if i+1<n and '10'<= s[i:i+2] <= '26':
                two = dp[i+2]
            dp[i] = one+two
        return dp[0]



     

















        