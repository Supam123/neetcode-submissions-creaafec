class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        why because n = 4 then we are calcualting the number of 1s
        for 0,1,2,3,4 which are total of 5 items hence 5 places in asnwer array
        i = 6 = 1 1 0
        chop last bit 6 >> 1 = 11 (3)
        3 has two ones 
        6 has two ones
        i = 5 = 1 0 1
        chop last bit 5>>1 = 10 (2)
        5 has 2 ones 
        2 has 1 one 
        so the pattern ins ans[i] = ans [i >> 1] + 1 or 0 depeneding on the last bit i had
        if it was 1 then its same plus 1
        if it was 0 then its same plus 0 basically i & 1
        '''
        ans = [0]*(n+1)
        for i in range(1,n+1):
            ans[i] =  ans[i>>1] + (i&1)
        return ans


