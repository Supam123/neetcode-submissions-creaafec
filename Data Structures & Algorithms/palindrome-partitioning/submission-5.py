class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        subset = []
        def isPalindrome(slice_s):
            l = 0
            r = len(slice_s) - 1
            while  l< r:
                if slice_s[l] != slice_s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        def dfs(i):
            if  i== len(s):
                res.append(subset.copy())
                return 
            
            for j in range(i,len(s)): 
                # given s = aab.
                #slice1 = a
                #slice2 = aa
                #slice 3 is discard not a plindrome
                slice_s = s[i:j+1]
                if isPalindrome(slice_s):
                    subset.append(slice_s) # add
                    dfs(j+1) #explore
                    subset.pop()
        dfs(0)
        return res

        