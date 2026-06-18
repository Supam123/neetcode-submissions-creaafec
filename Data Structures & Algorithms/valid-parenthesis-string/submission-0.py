class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        https://www.youtube.com/watch?v=cHT6sG_hUZI
        '''
        left_min,left_max = 0,0
        for i in range(len(s)):
            if s[i] == '(':
                left_min += 1
                left_max += 1
            elif s[i] == ')':
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            if left_min < 0:
                left_min = 0
            if left_max <0:
                return False # range doesnt evene exist
        return left_min == 0        