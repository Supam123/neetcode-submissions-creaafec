class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += str(len(i)) + '#' + i
        return s

    def decode(self, s: str) -> List[str]:
        length = ''
        i = 0
        o = []
        while i < len(s):
            if s[i] !=  '#':
                length += s[i]
                i+=1
            else:
                l = int(length)
                word = s[i+1: l+i+1]
                o.append(word)
                length = ''
                i = i + l + 1
            
        return o


