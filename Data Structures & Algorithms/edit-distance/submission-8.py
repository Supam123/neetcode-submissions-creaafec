class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row_below = [0]* (len(word2)+1)
        index = 0
        for j in range(len(word2),-1,-1):
            row_below[index] = j
            index+=1
        colIdx = 1
        for i in range(len(word1)-1,-1,-1):
            curr_row = [0]* (len(word2)+1)
            curr_row[-1] = colIdx
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    curr_row[j] = row_below[j+1]
                else:
                    curr_row[j] = 1 + min(curr_row[j+1],row_below[j],row_below[j+1])
            row_below = curr_row
            colIdx += 1
        return row_below[0]

























        # memo = {}
        # def dp(i,j):
        #     if i == len(word1) :
        #         return len(word2[j:])
        #     if j == len(word2) :
        #         return len(word1[i:])
        #     if (i,j) in memo:
        #         return memo[(i,j)]
            
        #     #match 
        #     insert,delete,replace =0,0,0 # when they match ist ZERO cost
        #     if word1[i] == word2[j]:
        #         memo[(i,j)] = dp(i+1,j+1)
        #     else:
        #         # we have 3 choices to find the minimum # way to make word1 -> word2
        #         insert = 1 + dp(i,j+1)
        #         delete = 1 + dp(i+1,j)
        #         replace = 1 + dp(i+1,j+1)

        #         memo[(i,j)] = min(insert, delete , replace)
        
        #     return memo[(i,j)]
        # return dp(0,0)
