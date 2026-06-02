class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(i,j):
            if i == len(word1) :
                return len(word2[j:])
            if j == len(word2) :
                return len(word1[i:])
            if (i,j) in memo:
                return memo[(i,j)]
            
            #match 
            insert,delete,replace =0,0,0 # when they match ist ZERO cost
            if word1[i] == word2[j]:
                memo[(i,j)] = dp(i+1,j+1)
            else:
                # we have 3 choices to find the minimum # way to make word1 -> word2
                insert = 1 + dp(i,j+1)
                delete = 1 + dp(i+1,j)
                replace = 1 + dp(i+1,j+1)

                memo[(i,j)] = min(insert, delete , replace)
        
            return memo[(i,j)]
        return dp(0,0)
