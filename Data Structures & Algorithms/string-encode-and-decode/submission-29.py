class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s  = s +str(len(i)) + "#" + i 
        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        length = ''
        i = 0
        while i < len(s):
            if s[i] != "#": 
                length += s[i]
                i += 1
            else:
                l = int(length)
                word = s[i+1 : i+l + 1]
                ans.append(word)
                i = i + l + 1
                length = ""
        return ans

