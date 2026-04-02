class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        hashmapT = {}
        hashmapS = {}
        res = ""
        res_len = float("inf")

        for i in range(len(t)):
            hashmapT[t[i]] =  hashmapT.get(t[i],0) + 1
        #hashmap = x:1 y:1 z:1
        have = 0
        need = len(hashmapT)
        while r < len(s):
            # need to add the window to hashmap
            # then check if my window is valid
            # if valid ... do somthen
            # if not valid keep adding
            hashmapS[s[r]] = hashmapS.get(s[r],0) + 1

            if s[r] in hashmapT and hashmapS[s[r]] == hashmapT[s[r]]:
                have += 1
            # now above ive built a check
            # a check that will tell me if my window is valid or not
            while have == need: # shrink it , why? cuz we want the minimum substring
                curr_len  = r-l+1
                if curr_len < res_len:
                    res_len = curr_len
                    res = s[l:r+1]

                hashmapS[s[l]] -= 1
                if s[l] in hashmapT and  hashmapS[s[l]] < hashmapT[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return res














        