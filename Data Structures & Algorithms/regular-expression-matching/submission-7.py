class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        row_below = [False] * (len(p)+1)
        row_below[-1] = True
        for j in range(len(p)-1,-1,-1):
            if j+1 < len(p) and p[j+1] == '*':
                row_below[j] =  row_below[j+2]
        for i in range(len(s)-1,-1,-1):
            curr_row = [False] * (len(p)+1)
            for j in range(len(p)-1,-1,-1):
                match = (s[i]==p[j] or p[j]=='.')
                if j+1 < len(p) and p[j+1] == '*':
                    if match and row_below[j]:
                        curr_row[j] = True
                    elif curr_row[j+2]:
                        curr_row[j] = True
                    else:
                        curr_row[j] = False          
                else:
                    if match:
                        curr_row[j] = row_below[j+1]
                    else:
                        curr_row[j] =  False
            row_below = curr_row
        return row_below[0]

        
     





















        # memo = {}
        # def dp(i,j):
        #     if i >= len(s) and j >= len(p):
        #         return True
        #     if j >= len(p):
        #         return False
        #     if(i,j) in memo:
        #         return memo[(i,j)]
        #     res = False
        #     match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        #     #check for *
        #     if j+1 < len(p) and p[j+1] == '*':
        #         take = match and dp(i+1,j) # use the star 
        #         skip = dp(i,j+2) #we dont use the star
        #         res = take or skip
            
        #     elif match:
        #         res = dp(i+1,j+1)
        #     memo[(i,j)] = res
        #     return memo[(i,j)]
        # return dp(0,0)
          
