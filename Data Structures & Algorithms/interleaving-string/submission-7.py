class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        s1 = "aaaa", 
        s2 = "bbbb", 
        s3 = "aabbbbaa"
        '''
        if len(s1) + len(s2) != len(s3):
            return False
        
        row_below = [False] * (len(s2) + 1)
        row_below[-1] = True
        for j in range(len(s2)-1,-1,-1):
            if s3[len(s1)+j] == s2[j]:
                row_below[j] = row_below[j+1]



        for i in range(len(s1)-1,-1,-1):
            curr_row = [False] * (len(s2) + 1)
            for j in range(len(s2),-1,-1):
                if j< len(s2) and s3[i+j] == s2[j] and curr_row[j+1] :
                    curr_row[j] = True

                if i< len(s1) and s3[i+j] == s1[i]  and row_below[j]  :
                    curr_row[j] = True
            row_below = curr_row
        return row_below[0]

                
                










































        # if len(s3) != (len(s1) + len(s2)):
        #     return False
        # memo = {}
        # def dp(i,j):
        #     if i == len(s1) and j == len(s2):
        #         return True # we proceedes all chars in both strings hence true
        #     if (i,j) in memo:
        #         return memo[(i,j)]
            
        #     if i < len(s1) and s3[i+j] == s1[i]:
        #         if dp(i+1,j): # if this path leads to true memo set to true return treu STOP we done
        #             memo[(i,j)] = True
        #             return True # stop we are done
        #     if j < len(s2) and s3[i+j] == s2[j]:
        #         if dp(i,j+1): # if this leads to a True path set memo to true return true we are done
        #             memo[(i,j)] = True
        #             return True
        #     # But if neither of the dp recursive calls are truer we never enter the if block
        #     # we never enter and return true so we set memo at that to false
        #     memo[(i,j)] = False
        #     return memo[(i,j)]
        # return dp(0,0)
            
        