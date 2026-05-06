class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        longest = 0
        r= 0
        while r  < len(s):
            if s[r] in hashmap:
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1

            while hashmap[s[r]] > 1:
                hashmap[s[l]] -= 1
                l += 1
            
            longest = max(longest,r-l+1)
            r += 1
        return longest
