class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            ans = 0
            while n > 0:
                digit =  n % 10
                digit =  digit**2
                ans += digit
                n = n // 10
            return ans
        slow,fast = n, get_next(n)
        while slow!=fast:
            slow = get_next(slow)
            fast  = get_next(get_next(fast))
        return True if fast == 1 else False


        