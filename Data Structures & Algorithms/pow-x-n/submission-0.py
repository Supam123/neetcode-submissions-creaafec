class Solution:
    def myPow(self, x: float, n: int) -> float:

        def dfs(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            ans  = dfs(x,n//2)
            if n%2 == 0:
                return ans * ans
            else:
                return ans * ans * x
        res =  dfs(x,abs(n))
        return res if n > 0 else 1/res