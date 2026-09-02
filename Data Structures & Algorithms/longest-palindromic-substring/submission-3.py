class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = ''
        for i in range(len(s)):
            l,r = i,i
            #odd 
            while l > -1 and r < len(s) and s[l] == s[r]:
                curr_len = r-l+1
                if curr_len > longest:
                    res = s[l:r+1]
                    longest = curr_len
                
                l -= 1
                r += 1
            
            #even 
            l,r = i,i+1
            while l>-1 and r<len(s) and s[l] == s[r]:
                curr_len = r-l+1
                if curr_len > longest:
                    res = s[l:r+1]
                    longest = curr_len
                l -= 1
                r += 1
        return res


