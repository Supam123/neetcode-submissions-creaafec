class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            bit = n & 1 # first we grab the right most bit
            res = res <<  1 # then we create space for this bit
            res =  res | bit  # we drop that bit
            n =  n >> 1# we discard that grabbed rightmost bit and move to the next one
        return res
        