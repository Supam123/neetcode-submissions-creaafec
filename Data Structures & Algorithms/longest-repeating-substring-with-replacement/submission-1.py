class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        longest = 0
        hashmap = {}
        while  r < len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
            else:
                hashmap[s[r]] += 1
            
            #rule=  window size - count of most freq number
            # if that is greater than k magic winds then its invalid
            maxFreq = max(hashmap.values())
            rule = (r-l+1) - maxFreq
            while rule > k:
                
                hashmap[s[l]] -= 1
                l += 1
                maxFreq = max(hashmap.values())
                rule = (r-l+1) - maxFreq
            longest = max(longest, r-l+1)
            r += 1
        return longest

          
        