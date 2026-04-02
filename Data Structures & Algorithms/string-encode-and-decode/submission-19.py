class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i 
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        length = ""
        res = []
        while i< len(s):
            if s[i] != '#':
                length += s[i]
                i += 1
            else:
                # when s[i] is equal to # that means 
                # we got the length and we are the start of the word
                l = int(length)
                word = s[i+1 : i+ l +1]
                i = i + l + 1
                length = ''
                res.append(word)
        return res
                
           
