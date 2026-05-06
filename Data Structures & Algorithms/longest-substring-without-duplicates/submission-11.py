class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()

        l = 0 
        r = 0
        longest = 0     
        while r < len(s):
            #window is sick and invalid
            while s[r] in myset:
                myset.remove(s[l]) # because we want a substring 
                l += 1
            myset.add(s[r])
            longest = max(longest, r-l+1)
            r +=1
        return longest 
       
        