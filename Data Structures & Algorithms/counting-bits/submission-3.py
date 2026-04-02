class Solution:
    def countBits(self, n: int) -> List[int]:
        # THIS IS O(nlogn)
        # output = []
        # def countIt(n):
        #     count = 0
        #     while n>0:
        #         if(n&1==1):
        #             count+=1
        #         n=n>>1
        #     return count
        # for i in range(n+1):
        #     res = countIt(i)
        #     output.append(res)
        # return output
        dp = [0] *(n+1)
        offset=1
        for n in range(1,n+1):
            if((offset * 2) == n):
                offset = n
            dp[n] = 1+ dp[n-offset]
        return dp 


        
        