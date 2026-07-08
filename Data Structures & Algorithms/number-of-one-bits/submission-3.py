class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count
        '''
        example 
        1= 10111 
           00001
           00001 count becomes 1
        then i shift 10111 >>1 = 01011
        2 = 01011 
            00001
            00001 count beomces 2
        then i shift 01011 >> 1 =  00101
        3 = 00101 & 1
            00001
            00001 count becomes 3
        then i shift 00101>>1  - 000100
        4 = 000100  & 1
            000001
            becoems 0 count stayes 3
            move right
            000010
        5  = 000010 & 1 count satsyes dsame move right
        6 =  000001 & 1 count becomes 4
        move right 000000 > 0 no we stop
           
        '''