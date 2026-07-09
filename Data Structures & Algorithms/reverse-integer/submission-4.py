class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign  = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            bit =  x % 10 # last bit
            ans = ans * 10 # move left create space
            ans =  ans + bit  # drop that bit 
            x = x // 10
        ans = ans*sign
        if (-2**31) <= ans <= (2**31 - 1):
            return ans
        else:
            return 0

        